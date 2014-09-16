-module(ex2_3).
-export([make_sample_tree/0, test_insert/0, test_traverse/0, test_member/0]).

-record(treenode, {key, value}).
-record(tree, {left, treenode=#treenode{}, right}).

make_node(K, V) ->
    TN = #treenode{key=K, value=V},
    T = #tree{treenode=TN},
    T.

make_node(K, V, LeftTree, RightTree) ->
    TN = #treenode{key=K, value=V},
    T = #tree{treenode=TN, left=LeftTree, right=RightTree},
    T.

insert_tree_node(undefined, K, V) ->
    make_node(K, V);
insert_tree_node(#tree{left=LT, treenode=#treenode{key=CurK, value=_CurV}, right=_RT}=T, K, V) when K < CurK  ->
    LT1=insert_tree_node(LT, K, V),
    T1=T#tree{left=LT1},
    T1;
insert_tree_node(#tree{left=_LT, treenode=#treenode{key=CurK, value=_CurV}, right=RT}=T, K, V) when K > CurK  ->
    RT1=insert_tree_node(RT, K, V),
    T1=T#tree{right=RT1},
    T1;
% when K == CurK
insert_tree_node(T, _K, V)  when is_record(T, tree) ->
    T#tree{treenode=#treenode{value=V}}.


traverse(F, Tree) when is_record(Tree, tree) and is_function(F) -> 
    traverse(F, Tree, 0).
traverse(_F, undefined, _D) -> ok;
traverse(F, Tree, D) when is_record(Tree, tree) and is_function(F) -> % F is a function that work on K and V
    traverse(F, Tree#tree.left, D+1),
    F(Tree#tree.treenode#treenode.key, Tree#tree.treenode#treenode.value, D),
    traverse(F, Tree#tree.right, D+1).

member(K, #tree{treenode=#treenode{key=K}}=Tree) -> 
    found;
member(K, #tree{treenode=#treenode{key=CurK}}=Tree) when K < CurK -> 
    io:format("Compared for ~p~n", [K]),
    member(K, Tree#tree.left);
member(K, #tree{treenode=#treenode{key=CurK}}=Tree) when K > CurK -> 
    io:format("Compared for ~p~n", [K]),
    member(K, Tree#tree.right);
member(K, undefined) ->
    not_found.

cmp_int(A, B) when A < B ->
    less_than;
cmp_int(A, B) when A > B ->
    bigger_than;
cmp_int(A, B) ->
    equal.

member(K, #tree{treenode=#treenode{key=K}}=Tree, _CmpFunc) -> 
    found;
member(K, #tree{treenode=#treenode{key=CurK}}=Tree) when K < CurK -> 
    io:format("Compared for ~p~n", [K]),
    
    member(K, Tree#tree.left);
    member(K, Tree#tree.right);
member(K, undefined) ->
    not_found.

%% routines for testings
%% 
make_sample_tree() ->
    Left = make_node(1, 1),
    Right = make_node(5, 5),
    T = make_node(3, 3, Left, Right),
    T.

make_sample_tree2() ->
    T = make_node(5, 5),
    T1 = insert_tree_node(T, 1, 1),
    T2 = insert_tree_node(T1, 2, 2),
    T3 = insert_tree_node(T2, 7, 7),
    T4 = insert_tree_node(T3, 6, 6),
    T5 = insert_tree_node(T4, 10, 10),
    T6 = insert_tree_node(T5, 12, 12),
    T6.
     
test_insert() ->
    T = make_sample_tree(),
    T1 = insert_tree_node(T, 7, 7),
    io:format("old ~p~n", [T]),
    io:format("new ~p~n", [T1]).

test_traverse() ->
    F = fun (K, V, _D) -> io:format("key:~p val:~p~n", [K, V]) end,
    T = make_sample_tree(),
    traverse(F, T).

test_member() ->
    T = make_sample_tree2(),
    F = fun (K, V, Depth) ->
            Indent = string:chars($\s, Depth*4), 
            io:format("~skey:~p val:~p~n", [Indent, K, V]) 
        end,
    traverse(F, T),
    R1 = member(12, T),
    R2 = member(-1, T),
    io:format("R1:~p R2:~p~n", [R1, R2]).
