export type QuestionItem = {
  questionText: string;
  questionType: string;
};

export type ModulePayload = {
  id: string;
  title: string;
  summaryText: string;
  questions: QuestionItem[];
};

export type ModuleEditorState = {
  moduleId: string;
  title: string;
  summaryText: string;
  questions: QuestionItem[];
  isSaving: boolean;
  isDirty: boolean;
};

export function createModuleEditorState(module: ModulePayload): ModuleEditorState {
  return {
    moduleId: module.id,
    title: module.title,
    summaryText: module.summaryText,
    questions: module.questions,
    isSaving: false,
    isDirty: false,
  };
}

export function setDirty(state: ModuleEditorState): ModuleEditorState {
  return { ...state, isDirty: true };
}

export function setSaving(state: ModuleEditorState, isSaving: boolean): ModuleEditorState {
  return { ...state, isSaving };
}

export function applyOptimisticSavedState(
  state: ModuleEditorState,
  saved: Pick<ModulePayload, "title" | "summaryText" | "questions">,
): ModuleEditorState {
  return {
    ...state,
    title: saved.title,
    summaryText: saved.summaryText,
    questions: saved.questions,
    isSaving: false,
    isDirty: false,
  };
}
