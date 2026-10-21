import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]/'skills/live-training-session-design'
spec=importlib.util.spec_from_file_location('validation',ROOT/'scripts/validate_course.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
BASE=json.loads((ROOT/'examples/workplace-communication-workshop.course.json').read_text())
class ValidationTests(unittest.TestCase):
 def setUp(self):self.d=copy.deepcopy(BASE)
 def errors(self):return v.validate_course(self.d,ROOT/'examples')
 def reject(self,phrase):self.assertTrue(any(phrase in e for e in self.errors()),self.errors())
 def test_valid_draft(self):self.assertEqual(self.errors(),[])
 def test_break_miscount(self):self.d['instructional_minutes']=90;self.reject('Instructional minutes')
 def test_overload(self):self.d['total_minutes']=60;self.reject('Agenda row total')
 def test_substep_overrun(self):self.d['agenda'][0]['substeps'][0]['minutes']=20;self.reject('substep minutes')
 def test_time_gap(self):self.d['agenda'][1]['start_minute']=12;self.reject('start time')
 def test_missing_practice_fact(self):del self.d['practices'][1]['facts']['deadline'];self.reject('missing practice fact')
 def test_fact_drift(self):self.d['practices'][1]['facts']['deadline']='noon Friday';self.reject('missing from Markdown')
 def test_unmapped_objective(self):self.d['objectives'][0]['assessment_ids']=[];self.reject('missing assessment_ids')
 def test_unknown_source(self):self.d['assessments'][0]['source_id']='S-999';self.reject('unknown source')
 def test_score_cannot_buy_critical_failure(self):self.d['assessments'][2]['score_examples'][1]['expected_pass']=True;self.reject('scoring rule mismatch')
 def test_invention_overrides_score(self):self.d['assessments'][2]['score_examples'][2]['expected_pass']=True;self.reject('scoring rule mismatch')
 def test_invalid_threshold(self):self.d['assessments'][2]['threshold']=6;self.reject('invalid threshold')
 def test_pass_without_evidence(self):self.d['quality_checks'][0]['evidence']=[];self.reject('Pass needs')
 def test_stale_review(self):self.d['quality_checks'][0]['artifact_version']='1.0.0';self.reject('stale review')
 def test_invalid_review_date(self):self.d['quality_checks'][0]['date']='last week';self.reject('ISO review date')
 def test_exclusion_is_not_pass(self):self.d['quality_checks'][-1]['status']='Pass';self.reject('exclusion needs')
 def test_required_check_cannot_be_excluded(self):self.d['quality_checks'][0].update(applicable=False,rationale='not convenient',status=None,evidence=[]);self.reject('cannot be excluded')
 def test_high_risk_requires_review(self):self.d['higher_risk']=True;self.reject('cannot be excluded')
 def test_software_requires_checks(self):self.d['software_training']=True;self.reject('cannot be excluded')
 def test_false_readiness(self):self.d['release_state']='Ready for delivery';self.reject('unperformed or failed checks');self.reject('delivery blockers')
 def test_defect_cannot_stay_draft(self):self.d['quality_checks'][0]['status']='Needs revision';self.reject('Material defect')
 def test_unsafe_path(self):self.d['quality_checks'][0]['evidence'][0]['path']='../../../../../etc/passwd';self.reject('unsafe local file')
 def test_bad_record(self):self.assertTrue(v.validate_course([],ROOT/'examples'))
 def test_missing_required_check(self):self.d['quality_checks'].pop();self.reject('check IDs differ')
 def test_duplicate_ids(self):self.d['agenda'][1]['id']='M-01';self.reject('unique')
 def test_markdown_drift(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);body=(ROOT/'examples'/BASE['document']).read_text().replace('| 0:08 | 12 |','| 0:08 | 15 |');(p/BASE['document']).write_text(body)
   self.assertTrue(any('Markdown agenda timing' in e for e in v.validate_course(self.d,p)))
 def test_untracked_placeholder(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);body=(ROOT/'examples'/BASE['document']).read_text()+'\n[TODO confirm owner]\n';(p/BASE['document']).write_text(body)
   self.assertTrue(any('Untracked placeholder' in e for e in v.validate_course(self.d,p)))
 def test_supporting_fact_drift(self):self.d['supporting_documents'][0]['required_quotes'].append('fictional missing deadline');self.reject('Supporting document is missing')
 def test_answer_key_separation(self):self.d['supporting_documents'][0]['forbidden_quotes'].append('Morgan Chen');self.reject('Supporting document contains forbidden')
 def test_missing_package_link(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);(p/'SKILL.md').write_text('---\nname: demo\ndescription: Test\n---\n[Missing](references/missing.md)');(p/'agents').mkdir();(p/'agents/openai.yaml').write_text('interface: {}')
   self.assertTrue(any('missing/unsafe link' in e for e in v.validate_package(p)))
if __name__=='__main__':unittest.main(verbosity=2)
