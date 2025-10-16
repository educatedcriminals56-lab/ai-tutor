
from fastapi import FastAPI, HTTPException
from models import DialogueRequest, DialogueResponse
from services.text_processor import preprocess_text
from services.fallacy_detector import detect_fallacies
from services.llm_service import get_socratic_questions
from services.dialogue_analyzer import DialogueAnalyzer

app = FastAPI(title="Project Socrates API")
analyzer = DialogueAnalyzer()

@app.get("/")
async def root():
    return {"status": "ok", "service": "Project Socrates"}

@app.post("/dialogue", response_model=DialogueResponse)
async def dialogue_endpoint(req: DialogueRequest):
    try:
        raw = req.question.strip()
        if not raw:
            raise HTTPException(status_code=400, detail="Empty question")

        processed = preprocess_text(raw)
        fallacies = detect_fallacies(processed)
        questions = await get_socratic_questions(processed, complexity=req.complexity)
        trace = analyzer.start_trace(raw, processed, fallacies)
        trace.add_ai_questions(questions)

        return DialogueResponse(
            response=questions[0] if questions else "Can you say more about that?",
            processed_input=processed,
            reasoning_trace=trace.to_dict(),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
