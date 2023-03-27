from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from classes.arena import Arena
from classes.equipment import Equipment
from classes.unit import PlayerUnit, EnemyUnit
from classes.unit_classes import unit_classes

app = Flask(__name__)

heroes = {
    "player": NotImplemented,
    "enemy": NotImplemented
}

arena = Arena()


@app.route("/")
def start_page():
    return render_template("index.html")


@app.route("/fight/")
def start_fight():
    """
    выполняет функцию start_game экземпляра класса арена и передаем ему необходимые аргументы
    рендерит экран боя (шаблон fight.html)
    """
    arena.start_game(player=heroes["player"], enemy=heroes["enemy"])
    return render_template('fight.html', heroes=heroes)


@app.route("/fight/hit")
def hit():
    """
    кнопка нанесения удара
    обновляет экран боя (нанесение удара) (шаблон fight.html)
    если игра идет - вызываем метод player.hit() экземпляра класса арены
    если игра не идет - пропускаем срабатывание метода (просто рендерит шаблон с текущими данными)
    """
    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.battle_result

    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/use-skill")
def use_skill():
    """кнопка использования скилла"""
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.battle_result

    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/pass-turn")
def pass_turn():
    """кнопка пропус хода"""
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.battle_result

    return render_template('fight.html', heroes=heroes, result=result)


@app.route("/fight/end-fight")
def end_fight():
    """кнопка завершить игру - переход в главное меню"""
    return render_template("index.html")


@app.route("/choose-hero/", methods=["POST", "GET"])
def choose_hero():
    """
    кнопка выбор героя. 2 метода GET и POST
    на GET отрисовывает форму.
    на POST отправляет форму и делаем редирект на эндпоинт choose enemy
    """
    if request.method == "GET":
        header = "Выберите героя"
        equipment = Equipment()
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        result = {
            "header": header,
            "weapons": weapons,
            "armors": armors,
            "classes": unit_classes
        }
        return render_template("hero_choosing.html", result=result)
    if request.method == "POST":
        name = request.form["name"]
        weapon_name = request.form["weapon"]
        armor_name = request.form["armor"]
        unit_class = request.form["unit_class"]
        player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class))
        player.equip_armor(Equipment().get_armor(armor_name))
        player.equip_weapon(Equipment().get_weapon(weapon_name))
        heroes["player"] = player
        return redirect(url_for("choose_enemy"))


@app.route("/choose-enemy/", methods=["POST", "GET"])
def choose_enemy():
    """
    кнопка выбор соперников. 2 метода GET и POST
    также на GET отрисовывает форму.
    а на POST отправляет форму и делаем редирект на начало битвы
    """
    if request.method == "GET":
        header = "Выберите противника"
        equipment = Equipment()
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        result = {
            "header": header,
            "weapons": weapons,
            "armors": armors,
            "classes": unit_classes
        }
        return render_template("hero_choosing.html", result=result)
    if request.method == "POST":
        name = request.form["name"]
        weapon_name = request.form["weapon"]
        armor_name = request.form["armor"]
        unit_class = request.form["unit_class"]
        enemy = EnemyUnit(name=name, unit_class=unit_classes.get(unit_class))
        enemy.equip_armor(Equipment().get_armor(armor_name=armor_name))
        enemy.equip_weapon(Equipment().get_weapon(weapon_name=weapon_name))
        heroes["enemy"] = enemy
        return redirect(url_for("start_fight"))
