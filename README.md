# Szegedfoglalo_tabla
##main finder commit


## Install

`pip install -r requirements.txt `
## Run

`python app.py`

## Request to "kviz"-question

```
method: "POST",
body: JSON.stringify({
    player:player_name,
    lobby: lobby,
    lap: lap,
    qtype:0,
    qtopic:0,
    qweights:0
})
```


## Response from "kviz"-question

```
<div class="question_box">
        <div>{{ lobby_question['question'] }}</div>
        <input type="radio" name="example" id="option1" value="1">
        <label id="answ1" for="option1">{{ lobby_question['answs']['answ1'] }}</label>
        <input type="radio" name="example" id="option2" value="2">
        <label id="answ2" for="option2">{{ lobby_question['answs']['answ2'] }}</label>
        <input type="radio" name="example" id="option3" value="3">
        <label id="answ3" for="option3">{{ lobby_question['answs']['answ3'] }}</label>
        <input type="radio" name="example" id="option4" value="4">
        <label id="answ4" for="option4">{{ lobby_question['answs']['answ4'] }}</label>
</div>
```

## Request to "kviz"-answer

```
method: "POST",
body: JSON.stringify({
    player:player_name,
    lobby: lobby,
    lap: lap,
    answ:parseInt(selectedValue)
})
```


## Response from "kviz"-answer

```
{
    'player':player_name,
    'lobby': lobby,
    'answer':lobby_question['Cor_answ']==answ,
    "pt":0
}
```

## Request to "kiertekeles"-result

```
method: "POST",
body: JSON.stringify({
    name: player1_name,
    id: player1_id,
    enemy: player2_name,
    lobby: lobby_name,
    lobby_id:lobby_id,
    pt1:player1_pt,
    pt2:player2_pt,
})
```


## Response from "kiertekeles"-result

```
<div class="box">
        <div id="input1">Név: {{ input1 }}</div>
        <br>
        <div id="input2">Ellenfél: {{ input2 }}</div>
        <br>
        <div id="input3">Lobby: {{ input3 }}</div>
        <br>
        <div id="input3">Válasz: {{ input4 }}</div>
        
        <a href="http://127.0.0.1:8000/lobby?player="
        onclick="location.href=this.href+'{{input1}}';return false;">
            <button id="newGame" onclick="test()"> Új játék </button> </a>
    </div>

```
