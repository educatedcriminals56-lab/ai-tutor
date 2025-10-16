
import uuid
from models import ReasoningTrace, Claim

class ReasoningNode:
    def __init__(self, text, source='user'):
        self.id=str(uuid.uuid4()); self.text=text; self.source=source
        self.assumptions=[]; self.contradictions=[]; self.fallacies=[]
    def to_claim(self): return Claim(id=self.id,text=self.text,source=self.source,
        assumptions=self.assumptions,contradictions=self.contradictions,fallacies=self.fallacies)

class DialogueAnalyzer:
    def __init__(self): self.traces={}
    def start_trace(self, raw_input, processed, fallacies):
        sid=str(uuid.uuid4())
        rt=ReasoningTrace(session_id=sid,original_input=raw_input,processed_input=processed,claims=[],ai_prompts=[])
        node=ReasoningNode(text=raw_input,source='user'); node.fallacies=fallacies; rt.claims.append(node.to_claim())
        self.traces[sid]=rt; return rt

def _patch_methods():
    def add_ai_questions(self, qs): self.ai_prompts.extend(qs)
    def to_dict(self): return {'session_id':self.session_id,'original_input':self.original_input,
        'processed_input':self.processed_input,'claims':[c.dict() for c in self.claims],'ai_prompts':self.ai_prompts}
    ReasoningTrace.add_ai_questions=add_ai_questions; ReasoningTrace.to_dict=to_dict
_patch_methods()
