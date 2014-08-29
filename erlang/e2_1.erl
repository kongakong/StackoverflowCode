-module(e2_1).

-export([suffixes/1]).

suffixes(L) -> suffixes(L, []).

suffixes([H|T], R) 
    -> suffixes(T, [[H|T]|R]);
suffixes([], R) -> lists:reverse([[]|R]).
