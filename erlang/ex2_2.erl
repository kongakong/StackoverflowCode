-module(ex2_2).
-export([make_sample_tree/0, test_insert/0]).

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

make_sample_tree() ->
    Left = make_node(1, 1),
    Right = make_node(5, 5),
    T = make_node(3, 3, Left, Right),
    T.

test_insert() ->
    T = make_sample_tree(),
    T1 = insert_tree_node(T, 7, 7),
    io:format("old ~p~n", [T]),
    io:format("new ~p~n", [T1]).

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
%% long hand to update the node value
% insert_tree_node(#tree{left=LT, treenode=#treenode{key=K, value=_CurV}=T, right=RT}, K, V) ->
%    #tree{left=LT, treenode=#treenode{key=K, value=V}, right=RT}.
insert_tree_node(T, _K, V)  when is_record(T, tree) ->
    T#tree{treenode=#treenode{value=V}}.
    
