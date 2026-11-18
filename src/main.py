from pathlib import Path
import pygame

ROOT = Path(__file__).resolve().parents[1]
SPRITES = ROOT / "assets" / "sprites"
STATES = ("idle", "keyboard", "mouse", "both", "blink")


def main():
    pygame.init()
    try:
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("BongoBuster - My Forever Player 2")
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 30)
        sprites = {}
        for state in STATES:
            path = SPRITES / f"{state}.png"
            if path.is_file():
                img = pygame.image.load(str(path)).convert_alpha()
                scale = min(600 / img.get_width(), 390 / img.get_height())
                sprites[state] = pygame.transform.smoothscale(
                    img, (max(1, round(img.get_width()*scale)), max(1, round(img.get_height()*scale)))
                )
        keys = set()
        buttons = set()
        elapsed = 0.0
        running = True
        while running:
            elapsed += clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    else:
                        keys.add(event.key)
                elif event.type == pygame.KEYUP:
                    keys.discard(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button in (1, 2, 3):
                    buttons.add(event.button)
                elif event.type == pygame.MOUSEBUTTONUP:
                    buttons.discard(event.button)
                elif event.type == pygame.WINDOWFOCUSLOST:
                    keys.clear()
                    buttons.clear()
            state = "both" if keys and buttons else "keyboard" if keys else "mouse" if buttons else "blink" if elapsed % 4.0 > 3.8 else "idle"
            screen.fill((25, 20, 36))
            sprite = sprites.get(state, sprites.get("idle"))
            if sprite is not None:
                screen.blit(sprite, sprite.get_rect(center=(320, 215)))
            else:
                pygame.draw.circle(screen, (155, 95, 220), (320, 215), 85)
                label = font.render("BUSTER", True, (255, 255, 255))
                screen.blit(label, label.get_rect(center=(320, 215)))
            label = font.render(f"Estado: {state}", True, (235, 225, 250))
            screen.blit(label, label.get_rect(center=(320, 420)))
            hint = font.render("Teclado / mouse | ESC para sair", True, (190, 180, 210))
            screen.blit(hint, hint.get_rect(center=(320, 450)))
            pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
