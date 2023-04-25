import random

import pygame

from tetris import constants
from tetris.piece import Piece


def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for x in range(constants.cols)] for x in range(constants.rows)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def convert_shape_format(piece):
    positions = []
    format = piece.shape[piece.rotation % len(piece.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                positions.append((piece.x + j, piece.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions


def valid_space(shape, grid):
    accepted_positions = [
        [(j, i) for j in range(constants.cols) if grid[i][j] == (0, 0, 0)]
        for i in range(constants.rows)
    ]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False

    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_piece():
    return Piece(5, 0, random.choice(constants.shapes))


def draw_grid(surface, row, col):
    sx = constants.top_left_x
    sy = constants.top_left_y
    for i in range(row):
        pygame.draw.line(
            surface,
            (128, 128, 128),
            (sx, sy + i * 30),
            (sx + constants.play_width, sy + i * 30),
        )  # horizontal lines
        for j in range(col):
            pygame.draw.line(
                surface,
                (128, 128, 128),
                (sx + j * 30, sy),
                (sx + j * 30, sy + constants.play_height),
            )  # vertical lines


def draw_window(surface, grid):
    surface.fill((0, 0, 0))
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("TETRIS", 1, (255, 255, 255))

    surface.blit(
        label,
        (constants.top_left_x + constants.play_width / 2 - (label.get_width() / 2), 30),
    )

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(
                surface,
                grid[i][j],
                (
                    constants.top_left_x + j * constants.block_size,
                    constants.top_left_y + i * constants.block_size,
                    constants.block_size,
                    constants.block_size,
                ),
                0,
            )

    pygame.draw.rect(
        surface,
        (255, 0, 0),
        (
            constants.top_left_x,
            constants.top_left_y,
            constants.play_width,
            constants.play_height,
        ),
        5,
    )

    draw_grid(surface, len(grid), len(grid[0]))
    pygame.display.update()


def main(win):
    global grid

    locked_positions = {}
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_piece()
    next_piece = get_piece()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= constants.fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotation = current_piece.rotation + 1 % len(
                        current_piece.shape
                    )
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(
                            current_piece.shape
                        )

                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_piece()
            change_piece = False

        draw_window(win, grid)

        if check_lost(locked_positions):
            run = False


if __name__ == "__main__":
    pygame.font.init()
    win = pygame.display.set_mode((constants.s_width, constants.s_height))
    pygame.display.set_caption("Tetris")
    main(win)  # start game
