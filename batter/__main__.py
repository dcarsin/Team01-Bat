import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    cast['paddle'] = []
    for x_crd in range(int(constants.MAX_X / 2), int(constants.MAX_X / 2) + constants.PADDLE_LENGTH):
        y_crd = int(constants.MAX_Y - 1)
        position = Point(x_crd, y_crd)
        piece = Actor()
        piece.set_text('=')
        piece.set_position(position)
        cast['paddle'].append(piece)

    cast["brick"] = []
    for x in range(5, 75):
        for y in range(2, 6):
            position = Point(x, y)
            brick = Actor()
            brick.set_text("*")
            brick.set_position(position)
            cast["brick"].append(brick)
    
    cast['wall_left'] = []
    for i in range(1, constants.MAX_Y):
        position = Point(1, i)
        wall_piece = Actor()
        wall_piece.set_text('')
        wall_piece.set_position(position)
        cast['wall_left'].append(wall_piece)

    cast['wall_right'] = []
    for i in range(1, constants.MAX_Y):
        position = Point(constants.MAX_X, i)
        wall_piece = Actor()
        wall_piece.set_text('')
        wall_piece.set_position(position)
        cast['wall_right'].append(wall_piece)


    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    #######
    velocity = Point(1, -1) # Initial direction of the ball
    #######
    ball = Actor()
    ball.set_text("@")
    ball.set_position(position)
    ball.set_velocity(velocity)
    cast["ball"] = [ball]
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)
