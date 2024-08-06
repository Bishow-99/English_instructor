

def teacher_response(openai, prompt):
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"system","content":"""You are expert in International English Language Testing System(IELTS),
                                        you need to do english conversation where you need to  ask 
                                         english question and I will answer that question, then you will evaluate my english response and ask another question """},
            {
             "role":"user", "content": str(prompt)
                    }
                ],
                temperature = 0.0
            )
    
    teachers_output = response.choices[0].message.content
    return teachers_output