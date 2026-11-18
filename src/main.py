from pathlib import Path
import random
import pygame

ROOT = Path(__file__).resolve().parents[1]
SPRITES = ROOT / "assets" / "sprites"

STATES = ("idle", "keyboard", "mouse", "both", "blink")

FPS = 60
MOUSE_TIMEOUT = 250
KEYBOARD_TIMEOUT = 150
BLINK_DURATION = 350
BLINK_MIN = 3000
BLINK_MAX = 6000


def main():
    pygame.init()

    try:
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption(
            "BongoBuster - My Forever Player 2"
        )

        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 30)
        sprites = {}

        # Carregamento dos sprites
        for state in STATES:
            path = SPRITES / f"{state}.png"

            if path.is_file():
                img = pygame.image.load(str(path)).convert_alpha()

                scale = min(
                    600 / img.get_width(),
                    390 / img.get_height()
                )

                sprites[state] = pygame.transform.smoothscale(
                    img,
                    (
                        max(1, round(img.get_width() * scale)),
                        max(1, round(img.get_height() * scale))
                    )
                )

        keys = set()
        buttons = set()

        mouse_until = 0
        keyboard_until = 0
        blink_until = 0

        next_blink = (
            pygame.time.get_ticks()
            + random.randint(BLINK_MIN, BLINK_MAX)
        )

        running = True

        while running:
            clock.tick(FPS)
            now = pygame.time.get_ticks()

            # Captura de eventos
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    else:
                        keys.add(event.key)
                        keyboard_until = now + KEYBOARD_TIMEOUT

                elif event.type == pygame.KEYUP:
                    keys.discard(event.key)

                elif event.type == pygame.MOUSEMOTION:
                    if event.rel != (0, 0):
                        mouse_until = now + MOUSE_TIMEOUT

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button in (1, 2, 3):
                        buttons.add(event.button)

                    mouse_until = now + MOUSE_TIMEOUT

                elif event.type == pygame.MOUSEBUTTONUP:
                    buttons.discard(event.button)

                elif event.type == pygame.MOUSEWHEEL:
                    mouse_until = now + MOUSE_TIMEOUT

                elif event.type == pygame.WINDOWFOCUSLOST:
                    keys.clear()
                    buttons.clear()
                    mouse_until = 0
                    keyboard_until = 0

            # Verificacao das atividades
            keyboard_active = bool(keys) or now < keyboard_until
            mouse_active = bool(buttons) or now < mouse_until

            # Controle dos estados
            if keyboard_active or mouse_active:
                blink_until = 0

                next_blink = now + random.randint(
                    BLINK_MIN, BLINK_MAX
                )

                if keyboard_active and mouse_active:
                    state = "both"
                elif keyboard_active:
                    state = "keyboard"
                else:
                    state = "mouse"

            else:
                if now >= next_blink:
                    blink_until = now + BLINK_DURATION

                    next_blink = blink_until + random.randint(
                        BLINK_MIN, BLINK_MAX
                    )

                state = "blink" if now < blink_until else "idle"

            # Renderizacao
            screen.fill((25, 20, 36))

            sprite = sprites.get(state)

            if sprite is None and state == "both":
                sprite = sprites.get("keyboard")

            if sprite is None:
                sprite = sprites.get("idle")

            if sprite is not None:
                screen.blit(
                    sprite,
                    sprite.get_rect(center=(320, 215))
                )
            else:
                pygame.draw.circle(
                    screen, (155, 95, 220), (320, 215), 85
                )

                label = font.render(
                    "BUSTER", True, (255, 255, 255)
                )

                screen.blit(
                    label,
                    label.get_rect(center=(320, 215))
                )

            label = font.render(
                f"Estado: {state}", True, (235, 225, 250)
            )

            screen.blit(
                label,
                label.get_rect(center=(320, 420))
            )

            hint = font.render(
                "Teclado / mouse | ESC para sair",
                True,
                (190, 180, 210)
            )

            screen.blit(
                hint,
                hint.get_rect(center=(320, 450))
            )

            pygame.display.flip()

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

