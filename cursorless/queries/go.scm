;; @statement generated by the following command:
;;  curl https://raw.githubusercontent.com/tree-sitter/tree-sitter-go/master/src/node-types.json | jq '[.[] | select(.type == "_statement" or .type == "_simple_statement") | .subtypes[].type]' | grep -v '\"_' | sed -n '1d;p' | sed '$d' | sort
;; and then cleaned up.
[
  (assignment_statement)
  ;; omit block for now, as it is not clear that it matches Cursorless user expectations
  ;; (block)
  (break_statement)
  (const_declaration)
  (continue_statement)
  (dec_statement)
  (defer_statement)
  (empty_statement)
  (expression_statement)
  (expression_switch_statement)
  (fallthrough_statement)
  (for_statement)
  (go_statement)
  (goto_statement)
  (if_statement)
  (inc_statement)
  (labeled_statement)
  (return_statement)
  (select_statement)
  (send_statement)
  (short_var_declaration)
  (type_declaration)
  (type_switch_statement)
  (var_declaration)
] @statement

[
  (interpreted_string_literal)
  (raw_string_literal)
] @string @textFragment

(comment) @comment @textFragment
