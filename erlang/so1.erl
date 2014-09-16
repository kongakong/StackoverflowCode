-module(so1).

-export([testurl/0,geturl/1]).

testurl() ->
    application:start(inets),
    geturl("http://www.afbudsrejser.dk").

geturl(Url)->
    {ok, RequestId} = httpc:request(get,
                        {Url,[{"User-Agent", "Opera/9.80 (Windows NT 6.1; U; ru) Presto/2.8.131 Version/11.10"}]}, 
                        [],
                        [{sync, false}]),
    {M, Header} = receive
        {http, {RequestId, {_HttpOk, ResponseHeaders, _Body}}} -> {ok, ResponseHeaders} 
      after 20000 ->
        {not_ok, err}
      end,
    io:format("httprequest to ~p: ~p ~p~n",[Url, M, Header]).
