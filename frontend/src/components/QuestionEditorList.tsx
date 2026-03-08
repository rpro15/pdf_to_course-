type QuestionItem = {
  questionText: string;
  questionType: string;
};

type QuestionEditorListProps = {
  questions: QuestionItem[];
  onChange: (questions: QuestionItem[]) => void;
};

export function QuestionEditorList({ questions, onChange }: QuestionEditorListProps) {
  const updateQuestion = (index: number, value: string) => {
    const next = [...questions];
    next[index] = { ...next[index], questionText: value };
    onChange(next);
  };

  return (
    <div>
      <h3>Questions</h3>
      {questions.map((question, index) => (
        <div key={index} style={{ marginBottom: 8 }}>
          <label>
            {question.questionType}
            <textarea
              value={question.questionText}
              onChange={(e) => updateQuestion(index, e.target.value)}
              rows={2}
              style={{ width: "100%" }}
            />
          </label>
        </div>
      ))}
    </div>
  );
}
