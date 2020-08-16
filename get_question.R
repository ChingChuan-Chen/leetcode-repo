library(pipeR)
library(stringr)
library(httr)

readme_md_file <- "README-all-list.md"
if (readme_md_file == "README.md") {
  md <- readLines(readme_md_file) %>>%
    str_extract_all("\\(((https|\\./Python|\\./Rust)[^)]+)\\)", simplify = TRUE)
} else if (readme_md_file == "README-all-list.md") {
  md <- readLines(readme_md_file) %>>%
    str_extract_all("\\(((https|\\./src-all/Python|\\./src-all/Rust)[^)]+)\\)", simplify = TRUE)
} else {
  stop("no such readme file!")
}

md <- md[md[,1] != "" & md[,3] != "", 1:3]

agent_name <- "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
question_data_url <- "https://leetcode.com/graphql"

cookies_leetcode <- c(
  "csrftoken" = "",
  "LEETCODE_SESSION" = ""
)

graphql_query <- "query questionData($titleSlug: String!) {
question(titleSlug: $titleSlug) {
questionId
questionFrontendId
boundTopicId
title
titleSlug
content
translatedTitle
translatedContent
isPaidOnly
difficulty
likes
dislikes
isLiked
similarQuestions
contributors {
username
profileUrl
avatarUrl
__typename
}
topicTags {
name
slug
translatedName
__typename
}
companyTagStats
codeSnippets {
lang
langSlug
code
__typename
}
stats
hints
solution {
id
canSeeDetail
paidOnly
__typename
}
status
sampleTestCase
metaData
judgerAvailable
judgeType
mysqlSchemas
enableRunCode
enableTestMode
enableDebugger
envInfo
libraryUrl
adminUrl
__typename
}
}
"

relace_all_html_tag <- function(x) {
  str_replace_all(x, "</?[^>]+>", "")
}



get_question <- function(title) {
  POST(
    question_data_url,
    body = list(operationName = "questionData", variables = list(titleSlug = title),
                query = graphql_query),
    encode = "json",
    content_type_json(),
    add_headers(origin="https://leetcode.com", referer=sprintf("https://leetcode.com/problems/%s/", title)),
    set_cookies(.cookies=cookies_leetcode),
    user_agent(agent_name)
  )
}

rs_main <- 'fn main() {
  assert_eq!(0, Solution::%s0));
  println!("Pass test cases!");
}'

listnode_rs <- '
// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}
//
impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

// helper function for test
pub fn from_vec(vec: Vec<i32>) -> Option<Box<ListNode>> {
    let mut current = None;
    for &v in vec.iter().rev() {
        let mut node = ListNode::new(v);
        node.next = current;
        current = Some(Box::new(node));
    }
    current
}'

tree_rs <- "
// Definition for a binary tree node
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub fn to_tree(vec: Vec<Option<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
    use std::collections::VecDeque;
    let head = Some(Rc::new(RefCell::new(TreeNode::new(vec[0].unwrap()))));
    let mut queue = VecDeque::new();
    queue.push_back(head.as_ref().unwrap().clone());

    for children in vec[1..].chunks(2) {
        let parent = queue.pop_front().unwrap();
        if let Some(v) = children[0] {
            parent.borrow_mut().left = Some(Rc::new(RefCell::new(TreeNode::new(v))));
            queue.push_back(parent.borrow().left.as_ref().unwrap().clone());
        }
        if children.len() > 1 {
            if let Some(v) = children[1] {
                parent.borrow_mut().right = Some(Rc::new(RefCell::new(TreeNode::new(v))));
                queue.push_back(parent.borrow().right.as_ref().unwrap().clone());
            }
        }
    }
    head
}"

pointe_rs <- '
#[derive(Debug, PartialEq, Eq)]
pub struct Point {
    pub x: i32,
    pub y: i32,
}

impl Point {
    #[inline]
    pub fn new(x: i32, y: i32) -> Self {
        Point { x, y }
    }
}'

py_main <- "
if __name__ == '__main__':
    assert Solution().%s0) == 0
"

listnode_py <- "
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
def from_list(vals: List[int]) -> ListNode:
    current = None
    for x in vals[::-1]:
        current = ListNode(x, current)
    return current

def to_list(list_node: ListNode) -> List[int]:
    vals = []
    while list_node is not None:
        vals.append(list_node.val)
        list_node = list_node.next
    return vals
"

tree_py <- "
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"

point_py <- "
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"

for (i in 1L:nrow(md)) {
  rsfile <- str_sub(md[i,2], 2L, -2L)
  if (!file.exists(rsfile)) {
    write("", rsfile)
  }
  pyfile <- str_sub(md[i,3], 2L, -2L)
  if (!file.exists(pyfile)) {
    write("", pyfile)
  }
  if ((file.size(rsfile) > 2) && (file.size(pyfile) > 2)) {
    next
  }
  
  question_title <- str_extract(md[i, 1], "/([^/]+)/\\)$") %>>% str_sub(2L, -3L)
  response <- get_question(question_title) 
  question_desc <- content(response)$data$question$content %>>% 
    relace_all_html_tag %>>% 
    str_replace_all("&gt;", ">") %>>%
    str_replace_all("&lt;", "<") %>>%
    str_replace_all("&nbsp;", " ") %>>%
    str_replace_all("\r\n", "\n") %>>%
    str_replace_all("(Example \\d+:|Constraints:|Follow up:|Note:)(\n)+", "\\1\n") %>>%
    str_replace_all("(\n){3,}", "\n\n")
  if (length(question_desc) == 0) {
    next
  }
  code_snippets <- do.call(rbind, content(response)$data$question$codeSnippets)

  if (file.size(rsfile) == 2) {
    write("/*", rsfile)
    write(question_desc, rsfile, append=TRUE)
    write("*/", rsfile, append=TRUE)
    if (any(code_snippets[,1]=="Rust")) {
      code <- code_snippets[code_snippets[,1]=="Rust", 3L]$code %>>%
        str_replace_all("//([^\n]+)\n", "")
      need_header <- str_detect(code, "Point|ListNode|TreeNode")
      if (need_header) {
        if (str_detect(code, "ListNode"))
          write(listnode_rs, rsfile, append=TRUE)
        if (str_detect(code, "TreeNode"))
          write(tree_rs, rsfile, append=TRUE)
        if (str_detect(code, "Point"))
          write(point_rs, rsfile, append=TRUE)
      }

      write("pub struct Solution {}", rsfile, append=TRUE)
      write(code, rsfile, append=TRUE)
      write("", rsfile, append = TRUE)
      main_name <- str_extract(code, "\\w+\\(")
      write(sprintf(rs_main, main_name), rsfile, append=TRUE)
    }
  }
  
  if (file.size(pyfile) == 2) {
    write('"""', pyfile)
    write(question_desc, pyfile, append=TRUE)
    write('"""', pyfile, append=TRUE)
    if (any(code_snippets[,1]=="Python3")) {
      code <- code_snippets[code_snippets[,1]=="Python3", 3L]$code %>>%
        str_replace_all("#([^\n]+)\n", "")
      need_header <- str_detect(code, "Point|ListNode|TreeNode")
      if (need_header) {
        if (str_detect(code, "ListNode"))
          write(listnode_py, pyfile, append=TRUE)
        if (str_detect(code, "TreeNode"))
          write(tree_py, pyfile, append=TRUE)
        if (str_detect(code, "Point"))
          write(point_py, pyfile, append=TRUE)
      }
      if (str_detect(code, "List\\[")) {
        write("from typing import List", pyfile, append=TRUE)
      }
      write(code, pyfile, append=TRUE)
      write("        pass\n", pyfile, append = TRUE)
      main_name <- str_extract(code, "\\w+\\(")
      write(sprintf(py_main, main_name), pyfile, append=TRUE)
    }
  }
  Sys.sleep(1)
}

