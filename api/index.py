from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


# Data quiz untuk 7 bab, tiap bab berisi list soal
quiz_data = {
    1: [
        {"question": "Huruf ini adalah …? (م)", "options": ["Mim", "Nun", "Dal", "Ra"], "answer": 1},
        {"question": "Huruf ini adalah …? (و)", "options": ["Waw", "Ha", "Jim", "Ba"], "answer": 1},
        {"question": "Huruf ini adalah …? (ح)", "options": ["Ha", "Kha", "Jim", "Dal"], "answer": 1},
        {"question": "Huruf ini adalah …? (ر)", "options": ["Ra", "Dal", "Sin", "Ta"], "answer": 1},
        {"question": "Huruf ini adalah …? (ف)", "options": ["Fa", "Qaf", "Kaf", "Ba"], "answer": 1},
        {"question": "Huruf ini adalah …? (ص)", "options": ["Shaad", "Saad", "Dal", "Ta"], "answer": 2},
        {"question": "Huruf ini adalah …? (غ)", "options": ["Ghoin", "Kha", "Ain", "Ha"], "answer": 1},
        {"question": "Huruf ini adalah …? (ط)", "options": ["Tha", "Tho", "To", "Tsa"], "answer": 3},
        {"question": "Huruf ini adalah …? (ل)", "options": ["Lam", "Mim", "Nun", "Ra"], "answer": 1},
        {"question": "Huruf ini adalah …? (ك)", "options": ["Kaf", "Qaf", "Kha", "Jim"], "answer": 1},
    ],
    # ... isi data bab 2-7 dengan struktur sama
  def quiz_bab1():
    print("\n=== Bab 1: Mengenal Huruf Hijaiyah ===\n")
    questions = [
        {"question": "Huruf ini adalah …? (م)", "options": ["1. Mim", "2. Nun", "3. Dal", "4. Ra"], "answer": "1"},
        {"question": "Huruf ini adalah …? (و)", "options": ["1. Waw", "2. Ha", "3. Jim", "4. Ba"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ح)", "options": ["1. Ha", "2. Kha", "3. Jim", "4. Dal"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ر)", "options": ["1. Ra", "2. Dal", "3. Sin", "4. Ta"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ف)", "options": ["1. Fa", "2. Qaf", "3. Kaf", "4. Ba"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ص)", "options": ["1. Shaad", "2. Saad", "3. Dal", "4. Ta"], "answer": "2"},
        {"question": "Huruf ini adalah …? (غ)", "options": ["1. Ghoin", "2. Kha", "3. Ain", "4. Ha"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ط)", "options": ["1. Tha", "2. Tho", "3. To", "4. Tsa"], "answer": "3"},
        {"question": "Huruf ini adalah …? (ل)", "options": ["1. Lam", "2. Mim", "3. Nun", "4. Ra"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ك)", "options": ["1. Kaf", "2. Qaf", "3. Kha", "4. Jim"], "answer": "1"},
    ]
    return run_quiz(questions)


def quiz_bab2():
    print("\n=== Bab 2: Mengenal Nama Huruf Hijaiyah ===\n")
    questions = [
        {"question": "Huruf ini namanya apa? (ب)", "options": ["1. Ba", "2. Ta", "3. Jim", "4. Dal"], "answer": "1"},
        {"question": "Huruf ini namanya apa? (ث)", "options": ["1. Tsa", "2. Ta", "3. Ha", "4. Jim"], "answer": "1"},
        {"question": "Huruf ini namanya apa? (ج)", "options": ["1. Jim", "2. Ha", "3. Kha", "4. Ba"], "answer": "1"},
        {"question": "Huruf ini namanya apa? (د)", "options": ["1. Dal", "2. Ra", "3. Ta", "4. Jim"], "answer": "1"},
        {"question": "Huruf ini namanya apa? (ذ)", "options": ["1. Dzal", "2. Dal", "3. Ra", "4. Ta"], "answer": "1"},
        {"question": "Huruf ini namanya apa? (ز)", "options": ["1. Zai", "2. Ra", "3. Jim", "4. Dal"], "answer": "1"},
        {"question": "Huruf ini namanya apa? (س)", "options": ["1. Sin", "2. Sad", "3. Ta", "4. Jim"], "answer": "1"},
        {"question": "Huruf ini namanya apa? (ش)", "options": ["1. Syin", "2. Sin", "3. Sad", "4. Ta"], "answer": "1"},
        {"question": "Huruf ini namanya apa? (ص)", "options": ["1. Sad", "2. Sin", "3. Ta", "4. Jim"], "answer": "1"},
        {"question": "Huruf ini namanya apa? (ض)", "options": ["1. Dad", "2. Sad", "3. Ta", "4. Jim"], "answer": "1"},
    ]
    return run_quiz(questions)


def quiz_bab3():
    print("\n=== Bab 3: Mengenal Bentuk Huruf Hijaiyah ===\n")
    questions = [
        {"question": "Huruf ini bentuk sambungnya apa? (كـ)", "options": ["1. Kaf", "2. Qaf", "3. Kha", "4. Jim"], "answer": "1"},
        {"question": "Huruf ini bentuk terpisahnya apa? (ح)", "options": ["1. Ha", "2. Kha", "3. Jim", "4. Dal"], "answer": "1"},
        {"question": "Huruf ini bentuk sambungnya apa? (لـ)", "options": ["1. Lam", "2. Mim", "3. Nun", "4. Ra"], "answer": "1"},
        {"question": "Huruf ini bentuk terpisahnya apa? (م)", "options": ["1. Mim", "2. Nun", "3. Dal", "4. Ra"], "answer": "1"},
        {"question": "Huruf ini bentuk sambungnya apa? (نـ)", "options": ["1. Nun", "2. Mim", "3. Dal", "4. Ra"], "answer": "1"},
        {"question": "Huruf ini bentuk terpisahnya apa? (ف)", "options": ["1. Fa", "2. Qaf", "3. Kaf", "4. Ba"], "answer": "1"},
        {"question": "Huruf ini bentuk sambungnya apa? (صـ)", "options": ["1. Shaad", "2. Saad", "3. Dal", "4. Ta"], "answer": "2"},
        {"question": "Huruf ini bentuk sambungnya apa? (طـ)", "options": ["1. Tha", "2. Tho", "3. To", "4. Tsa"], "answer": "3"},
        {"question": "Huruf ini bentuk sambungnya apa? (يـ)", "options": ["1. Ya", "2. Nun", "3. Mim", "4. Ra"], "answer": "1"},
        {"question": "Huruf ini bentuk terpisahnya apa? (ز)", "options": ["1. Zai", "2. Ra", "3. Jim", "4. Dal"], "answer": "1"},
    ]
    return run_quiz(questions)


def quiz_bab4():
    print("\n=== Bab 4: Pengucapan Huruf Hijaiyah ===\n")
    questions = [
        {"question": "Pengucapan huruf ب adalah …?", "options": ["1. Ba", "2. Ta", "3. Tha", "4. Jim"], "answer": "1"},
        {"question": "Pengucapan huruf ت adalah …?", "options": ["1. Ta", "2. Ba", "3. Tha", "4. Jim"], "answer": "1"},
        {"question": "Pengucapan huruf ث adalah …?", "options": ["1. Tsa", "2. Ta", "3. Sa", "4. Ha"], "answer": "1"},
        {"question": "Pengucapan huruf ج adalah …?", "options": ["1. Jim", "2. Ha", "3. Kha", "4. Ba"], "answer": "1"},
        {"question": "Pengucapan huruf ح adalah …?", "options": ["1. Ha", "2. Kha", "3. Jim", "4. Dal"], "answer": "1"},
        {"question": "Pengucapan huruf خ adalah …?", "options": ["1. Kha", "2. Ha", "3. Jim", "4. Dal"], "answer": "1"},
        {"question": "Pengucapan huruf د adalah …?", "options": ["1. Dal", "2. Ra", "3. Ta", "4. Jim"], "answer": "1"},
        {"question": "Pengucapan huruf ذ adalah …?", "options": ["1. Dzal", "2. Dal", "3. Ra", "4. Ta"], "answer": "1"},
        {"question": "Pengucapan huruf ر adalah …?", "options": ["1. Ra", "2. Dal", "3. Sin", "4. Ta"], "answer": "1"},
        {"question": "Pengucapan huruf ز adalah …?", "options": ["1. Zai", "2. Ra", "3. Jim", "4. Dal"], "answer": "1"},
    ]
    return run_quiz(questions)


def quiz_bab5():
    print("\n=== Bab 5: Huruf-Huruf yang Mirip Bentuknya ===\n")
    questions = [
        {"question": "Huruf ini adalah …? (ب)", "options": ["1. Ba", "2. Ta", "3. Tsa", "4. Jim"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ت)", "options": ["1. Ta", "2. Ba", "3. Tsa", "4. Jim"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ث)", "options": ["1. Tsa", "2. Ta", "3. Ba", "4. Jim"], "answer": "1"},
        {"question": "Huruf ini adalah …? (د)", "options": ["1. Dal", "2. Ra", "3. Ta", "4. Jim"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ذ)", "options": ["1. Dzal", "2. Dal", "3. Ra", "4. Ta"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ر)", "options": ["1. Ra", "2. Dal", "3. Sin", "4. Ta"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ز)", "options": ["1. Zai", "2. Ra", "3. Jim", "4. Dal"], "answer": "1"},
        {"question": "Huruf ini adalah …? (س)", "options": ["1. Sin", "2. Sad", "3. Ta", "4. Jim"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ش)", "options": ["1. Syin", "2. Sin", "3. Sad", "4. Ta"], "answer": "1"},
        {"question": "Huruf ini adalah …? (ص)", "options": ["1. Sad", "2. Sin", "3. Ta", "4. Jim"], "answer": "1"},
    ]
    return run_quiz(questions)


def quiz_bab6():
    print("\n=== Bab 6: Huruf-Huruf dengan Harakat ===\n")
    questions = [
        {"question": "Huruf ini dengan fatha adalah …? (بَ)", "options": ["1. Ba", "2. Bi", "3. Bu", "4. Ba (dengan Fatha)"], "answer": "4"},
        {"question": "Huruf ini dengan kasrah adalah …? (بِ)", "options": ["1. Ba", "2. Bi (dengan Kasrah)", "3. Bu", "4. Ba (dengan Fatha)"], "answer": "2"},
        {"question": "Huruf ini dengan dhammah adalah …? (بُ)", "options": ["1. Ba", "2. Bi", "3. Bu (dengan Dhammah)", "4. Ba (dengan Fatha)"], "answer": "3"},
        {"question": "Huruf ini dengan fatha adalah …? (تَ)", "options": ["1. Ta", "2. Ti", "3. Tu", "4. Ta (dengan Fatha)"], "answer": "4"},
        {"question": "Huruf ini dengan kasrah adalah …? (تِ)", "options": ["1. Ta", "2. Ti (dengan Kasrah)", "3. Tu", "4. Ta (dengan Fatha)"], "answer": "2"},
        {"question": "Huruf ini dengan dhammah adalah …? (تُ)", "options": ["1. Ta", "2. Ti", "3. Tu (dengan Dhammah)", "4. Ta (dengan Fatha)"], "answer": "3"},
        {"question": "Huruf ini dengan fatha adalah …? (ثَ)", "options": ["1. Tsa", "2. Tsi", "3. Tsu", "4. Tsa (dengan Fatha)"], "answer": "4"},
        {"question": "Huruf ini dengan kasrah adalah …? (ثِ)", "options": ["1. Tsa", "2. Tsi (dengan Kasrah)", "3. Tsu", "4. Tsa (dengan Fatha)"], "answer": "2"},
        {"question": "Huruf ini dengan dhammah adalah …? (ثُ)", "options": ["1. Tsa", "2. Tsi", "3. Tsu (dengan Dhammah)", "4. Tsa (dengan Fatha)"], "answer": "3"},
        {"question": "Huruf ini dengan fatha adalah …? (جَ)", "options": ["1. Ja", "2. Ji", "3. Ju", "4. Ja (dengan Fatha)"], "answer": "4"},
    ]
    return run_quiz(questions)


def quiz_bab7():
    print("\n=== Bab 7: Mengenal Huruf Hijaiyah dalam Kata Sederhana ===\n")
    questions = [
        {"question": "Huruf apa yang ada di awal kata ini? (بَابٌ)", "options": ["1. Ba", "2. Ta", "3. Jim", "4. Dal"], "answer": "1"},
        {"question": "Huruf apa yang ada di tengah kata ini? (كِتَابٌ)", "options": ["1. Ta", "2. Ba", "3. Kaf", "4. Jim"], "answer": "1"},
        {"question": "Huruf apa yang ada di akhir kata ini? (قَلَمٌ)", "options": ["1. Mim", "2. Lam", "3. Qaf", "4. Ba"], "answer": "1"},
        {"question": "Huruf apa yang ada di awal kata ini? (مَدْرَسَةٌ)", "options": ["1. Mim", "2. Dal", "3. Ra", "4. Sin"], "answer": "1"},
        {"question": "Huruf apa yang ada di tengah kata ini? (سَبْعٌ)", "options": ["1. Ba", "2. Ta", "3. Jim", "4. Dal"], "answer": "1"},
        {"question": "Huruf apa yang ada di akhir kata ini? (نَهْرٌ)", "options": ["1. Ra", "2. Nun", "3. Ha", "4. Dal"], "answer": "1"},
        {"question": "Huruf apa yang ada di awal kata ini? (رَجُلٌ)", "options": ["1. Ra", "2. Jim", "3. Lam", "4. Dal"], "answer": "1"},
        {"question": "Huruf apa yang ada di tengah kata ini? (فَرَسٌ)", "options": ["1. Ra", "2. Fa", "3. Sin", "4. Dal"], "answer": "1"},
        {"question": "Huruf apa yang ada di akhir kata ini? (كِتَابٌ)", "options": ["1. Ba", "2. Ta", "3. Kaf", "4. Jim"], "answer": "1"},
        {"question": "Huruf apa yang ada di tengah kata ini? (قَمَرٌ)", "options": ["1. Mim", "2. Qaf", "3. Ra", "4. Ba"], "answer": "1"},
    ]
    return run_quiz(questions)


def run_quiz(questions):
    score = 0
    for idx, q in enumerate(questions, 1):
        print(f"Nomor {idx}: {q['question']}")
        for opt in q["options"]:
            print(opt)
        answer = input("Jawaban kamu (masukkan nomor): ").strip()
        if answer == q["answer"]:
            print("Benar! 🎉\n")
            score += 1
        else:
            print(f"Salah! Jawaban yang benar: {q['answer']}\n")
    print(f"Quiz selesai! Skor kamu: {score}/{len(questions)}\n")
    return score


def main():
    print("=== Quiz Huruf Hijaiyah untuk Anak TPQ ===")
    print("Pilih bab untuk mulai quiz:")
    print("1. Mengenal Huruf Hijaiyah")
    print("2. Mengenal Nama Huruf Hijaiyah")
    print("3. Mengenal Bentuk Huruf Hijaiyah")
    print("4. Pengucapan Huruf Hijaiyah")
    print("5. Huruf-Huruf yang Mirip Bentuknya")
    print("6. Huruf-Huruf dengan Harakat")
    print("7. Mengenal Huruf Hijaiyah dalam Kata Sederhana")
    pilihan = input("Mas
}

@app.get("/")
async def root():
    return {"message": "API Quiz Huruf Hijaiyah siap!"}


@app.get("/quiz/{bab}", response_model=List[Question])
async def get_quiz(bab: int):
    if bab not in quiz_data:
        return []
    questions = quiz_data[bab]
    return [{"question": q["question"], "options": q["options"]} for q in questions]


@app.post("/quiz/submit", response_model=QuizResponse)
async def submit_quiz(data: QuizRequest):
    bab = data.bab
    user_answers = data.answers
    if bab not in quiz_data or len(user_answers) != len(quiz_data[bab]):
        return {"results": [], "score": 0, "total": 0}

    results = []
    score = 0
    for user_ans, correct_q in zip(user_answers, quiz_data[bab]):
        benar = (user_ans == correct_q["answer"])
        results.append(benar)
        if benar:
            score += 1

    return {"results": results, "score": score, "total": len(user_answers)}