
import asyncio
async def _local_question_generator(text, complexity='medium'):
    q = [f"You said: '{text}'. Could you restate your main claim in one sentence?"]
    if complexity in ('medium','high'): q.append('What assumptions does this rely on?')
    if complexity=='high': q.append('Can you think of a case where this might not hold?')
    else: q.append('Why do you believe that to be true?')
    await asyncio.sleep(0); return q
async def get_socratic_questions(processed_text, complexity='medium'):
    return await _local_question_generator(processed_text, complexity)
