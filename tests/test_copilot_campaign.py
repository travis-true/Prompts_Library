from pathlib import Path
import copy,importlib.util,json,tempfile,unittest,subprocess,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]/'skills/enablement-campaign-generator'
spec=importlib.util.spec_from_file_location('campaign_validator',ROOT/'scripts/validate_copilot_campaign.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
BASE=json.loads((ROOT/'examples/copilot/campaign.json').read_text())
class CampaignTests(unittest.TestCase):
 def test_valid_draft(self):self.assertEqual(v.validate(copy.deepcopy(BASE),ROOT),[])
 def test_skill(self):self.assertEqual(v.validate_skill(ROOT),[])
 def test_bad_record(self):self.assertEqual(v.validate([],ROOT),['Record must be object'])
 def test_collection_excluded(self):
  d=copy.deepcopy(BASE);d['metrics'][0].update(collection_status='Excluded; not collected',exclusion_rationale='No collection for this example');self.assertEqual(v.validate(d,ROOT),[])
 def test_metric_excluded(self):
  d=copy.deepcopy(BASE);d['tips'][0].update(metric_ids=[],measurement_exclusion='Single example; no response collection');self.assertEqual(v.validate(d,ROOT),[])
 def approved_fixture(self):
  d=copy.deepcopy(BASE);a=d['assets'][0];a['content_status']='Approved for this campaign';a['approval']=dict(path=a['path'],quote=a['quote'],method='Test fixture only',reviewer='Fictional test reviewer',date='2026-10-21',version=d['version'],content_sha256=hashlib.sha256((ROOT/a['path']).read_bytes()).hexdigest());return d
 def test_partial_approval_remains_draft(self):self.assertEqual(v.validate(self.approved_fixture(),ROOT),[])
 def test_approval_hash_mismatch(self):
  d=self.approved_fixture();d['assets'][0]['approval']['content_sha256']='bad';self.assertTrue(any('approved content hash differs' in x for x in v.validate(d,ROOT)))
 def test_rendered_visual_needs_file(self):
  d=copy.deepcopy(BASE);d['tips'][0]['visual']['status']='Rendered';self.assertTrue(any('rendered visual path missing' in x for x in v.validate(d,ROOT)))
 def test_rendered_visual_needs_hash(self):
  d=copy.deepcopy(BASE);d['tips'][0]['visual'].update(status='Rendered',rendered_path='examples/copilot/source-register.md');self.assertTrue(any('rendered visual hash differs' in x for x in v.validate(d,ROOT)))
 def test_rendered_visual_final_alt(self):
  d=copy.deepcopy(BASE);d['tips'][0]['visual']['status']='Rendered';self.assertTrue(any('final alt text missing' in x for x in v.validate(d,ROOT)))
 def test_cli_malformed(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'bad.json';p.write_text('{bad');r=subprocess.run([sys.executable,str(ROOT/'scripts/validate_copilot_campaign.py'),'--record',str(p)],capture_output=True,text=True);self.assertNotEqual(r.returncode,0);self.assertEqual(json.loads(r.stdout)['structural_validation'],'FAIL')
# Each mutation represents an independently broken campaign invariant.
CASES=[
 ('schema',lambda d:d.update(schema_version='0'),'Unsupported schema'),
 ('version',lambda d:d.update(version='0'),'Overview version differs'),
 ('release_state',lambda d:d.update(release_state='Ready for release'),'Overview state differs'),
 ('source_metadata',lambda d:d['sources'][0].update(publisher=''),'source metadata missing'),
 ('source_official',lambda d:d['sources'][0].update(url='https://example.com/claims'),'official Microsoft source'),
 ('source_date',lambda d:d['sources'][0].update(accessed='bad'),'invalid date'),
 ('source_quote',lambda d:d['sources'][0].update(quote='NOT-A-SOURCE-EXCERPT-991'),'source excerpt unresolved'),
 ('source_path',lambda d:d['sources'][0].update(path='absent.md'),'Missing/unsafe file'),
 ('claim_reference',lambda d:d['claims'][0].update(source_ids=['missing']),'unknown reference'),
 ('claim_scope',lambda d:d['claims'][0].update(scope='all products'),'invalid claim scope'),
 ('claim_dependency',lambda d:d['claims'][0].update(dependencies=''),'statement/dependencies'),
 ('claim_fake_environment',lambda d:d['claims'][0].update(environment_status='Pass'),'actual evidence missing'),
 ('claim_expiry',lambda d:(d.update(release_state='Ready for release'),d['claims'][0].update(refresh_by='2000-01-01')),'expired claim blocks'),
 ('unverified_claim_release',lambda d:(d.update(release_state='Ready for release'),d['claims'][0].update(documentation_status='Not verified')),'unverified claim blocks'),
 ('feature_no_tenant',lambda d:(d.update(release_state='Ready for release'),d['claims'][0].update(scope='feature')),'actual environment evidence'),
 ('sequence_count',lambda d:d['calendar'].update(count=29),'Calendar count differs'),
 ('sequence_order',lambda d:d['tips'][0].update(sequence=5),'sequence/order differs'),
 ('sequence_dates',lambda d:d['calendar'].update(start_date='2026-10-22'),'cannot imply dates'),
 ('dated_timezone',lambda d:d['calendar'].update(mode='dated',start_date='2026-10-22',timezone='invalid'),'valid timezone'),
 ('tip_duplicate',lambda d:d['tips'].append(copy.deepcopy(d['tips'][0])),'Tip IDs must be unique'),
 ('tip_stale',lambda d:d['tips'][0].update(version='old'),'stale tip version'),
 ('tip_scenario',lambda d:d['tips'][0].update(scenario=''),'missing tip scenario'),
 ('tip_inputs_missing',lambda d:d['tips'][0].update(inputs='MISSING-INPUT-991'),'inputs differs from file'),
 ('tip_model',lambda d:d['tips'][0].update(model='MISSING-MODEL-991'),'model differs from file'),
 ('tip_review',lambda d:d['tips'][0].update(review='MISSING-REVIEW-991'),'review differs from file'),
 ('tip_prerequisite',lambda d:d['tips'][0].update(prerequisite_ids=['TIP-030']),'unknown/future prerequisite'),
 ('tip_joiner',lambda d:d['tips'][0].update(new_joiner_path=''),'missing tip new_joiner'),
 ('tip_difficulty',lambda d:d['tips'][0].update(difficulty='Advocacy'),'invalid difficulty'),
 ('tip_difficulty_rationale',lambda d:d['tips'][0].update(difficulty_rationale=''),'missing tip difficulty_rationale'),
 ('tip_prompt_component',lambda d:d['tips'][0]['prompt'].pop('expectation'),'incomplete GCSE'),
 ('tip_prompt_source',lambda d:d['tips'][0]['prompt'].update(source='unsupplied file'),'prompt source differs'),
 ('tip_metric_reference',lambda d:d['tips'][0].update(metric_ids=['missing']),'unknown reference'),
 ('tip_metric_no_exclusion',lambda d:d['tips'][0].update(metric_ids=[]),'metric or exclusion'),
 ('duplicate_scenario',lambda d:d['tips'][1].update(scenario=d['tips'][0]['scenario']),'Duplicate task-specific scenario'),
 ('duplicate_expected',lambda d:d['tips'][1].update(model=d['tips'][0]['model']),'Duplicate task-specific model'),
 ('duplicate_review',lambda d:d['tips'][1].update(review=d['tips'][0]['review']),'Duplicate task-specific review'),
 ('duplicate_question',lambda d:d['tips'][1].update(question=d['tips'][0]['question']),'Duplicate task-specific question'),
 ('retrieval_missing',lambda d:[t.update(mode='new-task') for t in d['tips']],'retrieval/retry'),
 ('visual_image_prompt',lambda d:d['tips'][0]['visual'].update(image_prompt=''),'visual missing image_prompt'),
 ('visual_dimensions',lambda d:d['tips'][0]['visual'].update(width=0),'invalid dimensions'),
 ('visual_ratio',lambda d:d['tips'][0]['visual'].update(ratio='1:1'),'aspect ratio differs'),
 ('visual_brief_access',lambda d:d['tips'][0]['visual'].update(accessibility_status='Pass'),'brief cannot pass'),
 ('visual_unverified_release',lambda d:d.update(release_state='Ready for release'),'required visual not rendered'),
 ('channel_coverage',lambda d:d['assets'].pop(0),'channel coverage/duplicate'),
 ('channel_duplicate',lambda d:d['assets'].append(dict(d['assets'][0],id='EXTRA')),'channel coverage/duplicate'),
 ('channel_parent',lambda d:d['assets'][0].update(tip_id='missing'),'unknown parent tip'),
 ('channel_stale',lambda d:d['assets'][0].update(version='old'),'stale asset version'),
 ('channel_content',lambda d:d['assets'][0].update(quote='ABSENT-CONTENT-991'),'channel content unresolved'),
 ('channel_fake_approval',lambda d:d['assets'][0].update(content_status='Approved for this campaign'),'actual evidence missing'),
 ('channel_fake_publication',lambda d:d['assets'][0].update(publication_status='Published'),'publication requires approved asset'),
 ('channel_fake_schedule',lambda d:d['assets'][0].update(publication_status='Scheduled'),'schedule/execution identity missing'),
 ('channel_draft_release',lambda d:d.update(release_state='Ready for release'),'draft asset blocks'),
 ('channel_owner_release',lambda d:d.update(release_state='Ready for release'),'publishing owner unresolved'),
 ('channel_expired',lambda d:(d.update(release_state='Ready for release'),d['assets'][0].update(expires='2000-01-01')),'expired asset blocks'),
 ('metric_denominator',lambda d:d['metrics'][0].update(denominator=''),'metric missing denominator'),
 ('metric_population',lambda d:d['metrics'][0].update(population=''),'metric missing population'),
 ('metric_missingness',lambda d:d['metrics'][0].update(missingness=''),'metric missing missingness'),
 ('metric_owner',lambda d:d['metrics'][0].update(collection_owner=''),'metric missing collection_owner'),
 ('metric_retention',lambda d:d['metrics'][0].update(retention=''),'metric missing retention'),
 ('metric_learning',lambda d:d['metrics'][0].update(layer='Learning'),'attempt cannot establish learning'),
 ('metric_unknown_zero',lambda d:d['metrics'][0].update(baseline='unknown'),'numeric unknown must be null'),
 ('metric_target_authority',lambda d:d['metrics'][0].update(target=80),'target authority missing'),
 ('metric_fake_results',lambda d:d['metrics'][0].update(result=20),'actual evidence missing'),
 ('metric_collection',lambda d:d['metrics'][0].update(collection_status='Collected'),'actual evidence missing'),
 ('metric_exclusion_rationale',lambda d:d['metrics'][0].update(collection_status='Excluded; not collected'),'exclusion rationale missing'),
 ('metric_unapproved_ready',lambda d:d.update(release_state='Ready for release'),'Measurement plan needs authorization'),
 ('quality_coverage',lambda d:d['quality_checks'].pop(),'Fifteen individual'),
 ('quality_scope',lambda d:d['quality_checks'][0].update(scope=''),'scope/rationale/action'),
 ('quality_false_pass',lambda d:d['quality_checks'][4].update(status='Pass'),'actual evidence missing'),
 ('quality_stale',lambda d:d['quality_checks'][0].update(version='old'),'stale quality version'),
 ('quality_exclusion',lambda d:d['quality_checks'][-1].update(status='Pass'),'exclusion cannot Pass'),
 ('quality_exclusion_rationale',lambda d:d['quality_checks'][-1].update(rationale=''),'scope/rationale/action'),
 ('quality_known_defect',lambda d:d['quality_checks'][0].update(status='Needs revision'),'Known defect requires'),
 ('readiness_unperformed',lambda d:d.update(release_state='Ready for release'),'unperformed quality checks'),
 ('readiness_blockers',lambda d:d.update(release_state='Ready for release'),'blocking open items'),
 ('readiness_authorization',lambda d:d.update(release_state='Ready for release'),'Readiness requires actual authorization'),
 ('authorization_fake',lambda d:d['release_authorization'].update(status='Authorized'),'actual evidence missing'),
 ('handoff_destinations',lambda d:d['handoffs'][0].update(destination='other'),'destinations differ'),
 ('handoff_dispatch',lambda d:d['handoffs'][0].update(status='Executed'),'cannot imply execution'),
 ('handoff_ids',lambda d:d['handoffs'][0].update(tip_ids=['missing']),'unknown reference'),
 ('handoff_findings',lambda d:d['handoffs'][0].update(finding_ids=['F-991']),'handoff lost reference'),
 ('handoff_acceptance',lambda d:d['handoffs'][0].update(acceptance=''),'owner/tasks/acceptance missing'),
 ('unsafe_path',lambda d:d['sources'][0].update(path='../../../../../etc/passwd'),'unsafe file')]
for name,mutation,phrase in CASES:
 def case(self,mutation=mutation,phrase=phrase):
  d=copy.deepcopy(BASE);mutation(d);errors=v.validate(d,ROOT);self.assertTrue(any(phrase in x for x in errors),errors)
 setattr(CampaignTests,'test_'+name,case)
if __name__=='__main__':unittest.main(verbosity=2)
