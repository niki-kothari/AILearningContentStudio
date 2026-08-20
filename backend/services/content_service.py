from services.llm_service import get_llm

def generate_chapter_content(topic, chapter_name, subtopics, model_name):

    llm = get_llm(model_name)

    subtopic_text = ""
    for index, subtopic in enumerate(subtopics, start=1):
        subtopic_text += (
            f"{index}. {subtopic}\n"
        )

    prompt = f"""
    You are an expert educational content creator.

    Create COMPLETE educational content.

    MAIN TOPIC:
    {topic}

    CHAPTER:
    {chapter_name}

    IMPORTANT:
    Generate content STRICTLY ONLY for these subtopics: {subtopic_text}

    IMPORTANT INSTRUCTIONS:

   1. Do NOT add extra topics
    2. Do NOT generate unrelated concepts
    3. Follow the roadmap structure strictly
    4. Generate detailed explanations
    5. Add examples
    6. Add practical use cases
    7. Add exercises
    8. Add summary
    9. Beginner friendly
    10. Professional formatting

    The output should look like a real educational book chapter.
    """

    response = llm.invoke(prompt)

    return response.content
