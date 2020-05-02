Question link: https://stackoverflow.com/questions/61557527/how-to-get-a-th-inside-a-tr-with-beautifulsoup

Need to reinstall numpy due to catalina upgrade

    pip3 install --upgrade --force-reinstal numpy
    pip3 install --upgrade --force-reinstal pandas


Debug output:


<table class="general" id="tablaDatos">
<thead><tr><td class="th r0" rowspan="2"></td><th class="r0" id="c_A0">Índice</th></tr><tr><th class="r1 cols" headers="c_A0" id="c_B0">2019T4</th></tr></thead><tbody><tr><th class="s0" colspan="2" id="r_A1">Nacional</th>
<tr><th class="s1 rows" headers="r_A1" id="r_B1">General</th>
<td class="sd" headers="r_B1 c_B0"><!--{"f":1569880800000,"s":"IPV769"} -->125,320</td></tr><tr><th class="s0" colspan="2" id="r_A2">01 Andalucía</th>
<tr><th class="s1 rows" headers="r_A2" id="r_B2">General</th>
<td class="sd" headers="r_B2 c_B0"><!--{"f":1569880800000,"s":"IPV766"} -->118,553</td></tr><tr><th class="s0" colspan="2" id="r_A3">02 Aragón</th>
<tr><th class="s1 rows" headers="r_A3" id="r_B3">General</th>
<td class="sd" headers="r_B3 c_B0"><!--{"f":1569880800000,"s":"IPV763"} -->118,107</td></tr><tr><th class="s0" colspan="2" id="r_A4">03 Asturias, Principado de</th>
<tr><th class="s1 rows" headers="r_A4" id="r_B4">General</th>
<td class="sd" headers="r_B4 c_B0"><!--{"f":1569880800000,"s":"IPV760"} -->112,223</td></tr><tr><th class="s0" colspan="2" id="r_A5">04 Balears, Illes</th>
<tr><th class="s1 rows" headers="r_A5" id="r_B5">General</th>
<td class="sd" headers="r_B5 c_B0"><!--{"f":1569880800000,"s":"IPV757"} -->133,139</td></tr><tr><th class="s0" colspan="2" id="r_A6">05 Canarias</th>
<tr><th class="s1 rows" headers="r_A6" id="r_B6">General</th>
<td class="sd" headers="r_B6 c_B0"><!--{"f":1569880800000,"s":"IPV754"} -->118,344</td></tr><tr><th class="s0" colspan="2" id="r_A7">06 Cantabria</th>
<tr><th class="s1 rows" headers="r_A7" id="r_B7">General</th>
<td class="sd" headers="r_B7 c_B0"><!--{"f":1569880800000,"s":"IPV751"} -->117,029</td></tr><tr><th class="s0" colspan="2" id="r_A8">07 Castilla y León</th>
<tr><th class="s1 rows" headers="r_A8" id="r_B8">General</th>
<td class="sd" headers="r_B8 c_B0"><!--{"f":1569880800000,"s":"IPV748"} -->113,657</td></tr><tr><th class="s0" colspan="2" id="r_A9">08 Castilla - La Mancha</th>
<tr><th class="s1 rows" headers="r_A9" id="r_B9">General</th>
<td class="sd" headers="r_B9 c_B0"><!--{"f":1569880800000,"s":"IPV745"} -->108,241</td></tr><tr><th class="s0" colspan="2" id="r_A10">09 Cataluña</th>
<tr><th class="s1 rows" headers="r_A10" id="r_B10">General</th>
<td class="sd" headers="r_B10 c_B0"><!--{"f":1569880800000,"s":"IPV742"} -->135,113</td></tr><tr><th class="s0" colspan="2" id="r_A11">10 Comunitat Valenciana</th>
<tr><th class="s1 rows" headers="r_A11" id="r_B11">General</th>
<td class="sd" headers="r_B11 c_B0"><!--{"f":1569880800000,"s":"IPV739"} -->115,562</td></tr><tr><th class="s0" colspan="2" id="r_A12">11 Extremadura</th>
<tr><th class="s1 rows" headers="r_A12" id="r_B12">General</th>
<td class="sd" headers="r_B12 c_B0"><!--{"f":1569880800000,"s":"IPV736"} -->106,046</td></tr><tr><th class="s0" colspan="2" id="r_A13">12 Galicia</th>
<tr><th class="s1 rows" headers="r_A13" id="r_B13">General</th>
<td class="sd" headers="r_B13 c_B0"><!--{"f":1569880800000,"s":"IPV733"} -->113,514</td></tr><tr><th class="s0" colspan="2" id="r_A14">13 Madrid, Comunidad de</th>
<tr><th class="s1 rows" headers="r_A14" id="r_B14">General</th>
<td class="sd" headers="r_B14 c_B0"><!--{"f":1569880800000,"s":"IPV730"} -->140,469</td></tr><tr><th class="s0" colspan="2" id="r_A15">14 Murcia, Región de</th>
<tr><th class="s1 rows" headers="r_A15" id="r_B15">General</th>
<td class="sd" headers="r_B15 c_B0"><!--{"f":1569880800000,"s":"IPV727"} -->112,501</td></tr><tr><th class="s0" colspan="2" id="r_A16">15 Navarra, Comunidad Foral de</th>
<tr><th class="s1 rows" headers="r_A16" id="r_B16">General</th>
<td class="sd" headers="r_B16 c_B0"><!--{"f":1569880800000,"s":"IPV724"} -->111,887</td></tr><tr><th class="s0" colspan="2" id="r_A17">16 País Vasco</th>
<tr><th class="s1 rows" headers="r_A17" id="r_B17">General</th>
<td class="sd" headers="r_B17 c_B0"><!--{"f":1569880800000,"s":"IPV721"} -->118,272</td></tr><tr><th class="s0" colspan="2" id="r_A18">17 Rioja, La</th>
<tr><th class="s1 rows" headers="r_A18" id="r_B18">General</th>
<td class="sd" headers="r_B18 c_B0"><!--{"f":1569880800000,"s":"IPV718"} -->116,161</td></tr><tr><th class="s0" colspan="2" id="r_A19">18 Ceuta</th>
<tr><th class="s1 rows" headers="r_A19" id="r_B19">General</th>
<td class="sd" headers="r_B19 c_B0"><!--{"f":1569880800000,"s":"IPV715"} -->131,854</td></tr><tr><th class="s0" colspan="2" id="r_A20">19 Melilla</th>
<tr><th class="s1 rows" headers="r_A20" id="r_B20">General</th>
<td class="sd" headers="r_B20 c_B0"><!--{"f":1569880800000,"s":"IPV712"} -->126,218</td></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tr></tbody></table>
