import { ActionType } from "@cursorless/common";

/**
 * This is a mapping from action names to their default spoken forms, or `null`
 * if the action has no spoken form.
 */
export const actions = {
  scrollToBottom: "bottom",
  toggleLineBreakpoint: "break point",
  cutToClipboard: "carve",
  scrollToCenter: "center",
  clearAndSetSelection: "change",
  remove: "chuck",
  insertCopyBefore: "clone up",
  insertCopyAfter: "clone",
  toggleLineComment: "comment",
  copyToClipboard: "copy",
  scrollToTop: "crown",
  outdentLine: "dedent",
  revealDefinition: "define",
  editNewLineBefore: "drink",
  insertEmptyLineBefore: "drop",
  extractVariable: "extract",
  insertEmptyLineAfter: "float",
  foldRegion: "fold",
  followLink: "follow",
  deselect: "give",
  highlight: "highlight",
  showHover: "hover",
  indentLine: "indent",
  showDebugHover: "inspect",
  setSelectionAfter: "post",
  editNewLineAfter: "pour",
  setSelectionBefore: "pre",
  insertEmptyLinesAround: "puff",
  showQuickFix: "quick fix",
  showReferences: "reference",
  rename: "rename",
  reverseTargets: "reverse",
  findInWorkspace: "scout all",
  randomizeTargets: "shuffle",
  generateSnippet: "snippet make",
  sortTargets: "sort",
  setSelection: "take",
  revealTypeDefinition: "type deaf",
  unfoldRegion: "unfold",
  callAsFunction: "call",
  swapTargets: "swap",
  replaceWithTarget: "bring",
  moveToTarget: "move",
  wrapWithPairedDelimiter: "wrap",
  wrapWithSnippet: "wrap",
  rewrapWithPairedDelimiter: "repack",
  insertSnippet: "snippet",
  pasteFromClipboard: "paste",

  ["experimental.setInstanceReference"]: "from",

  editNew: null,
  executeCommand: null,
  getText: null,
  replace: null,

  // These actions are implemented talon-side, usually using `getText` followed
  // by some other action.
  // applyFormatter: "format",
  // findInDocument: "scout",
  // nextHomophone: "phones",
} as const satisfies Record<ActionType, string | null>;
