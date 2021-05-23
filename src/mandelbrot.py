import pygame

" CONSTANTS "
# Dimensions
WIDTH, HEIGHT = 400, 400
# Iterations per pixel
ITERATIONS = 100
# Colors
BLACK = (0, 0, 0)


def main():
    """
    Main function of the program
    """

    # Initialize pygame
    pygame.init()
    # Setup window
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    # Draw stuff on window
    draw(window)

    # Update window
    pygame.display.update()

    running = True
    while running:

        # Check if the user pressed the close button 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Quit pygame
    pygame.quit()


def draw(surface):
    """
    Draws onto the surface
    @param: pygame.Surface
    @return: None
    """

    # Draw background color
    surface.fill(BLACK)

    for i in range(HEIGHT):
        for j in range(WIDTH):

            # Normalize i, j to be within [-2, 2]
            z, c = normalize(i, 0, HEIGHT, -2, 2), normalize(j, 0, WIDTH, -2, 2)
            # Copies of original values of z & c
            orig_z, orig_c = z, c

            # Counts the iterations made for the given pixel
            n = 0
            for x in range(ITERATIONS):
                # z^2 - c^2
                tmp_z = z * z - c * c
                # 2zci
                tmp_c = 2 * z * c
                z = tmp_z + orig_z
                c = tmp_c + orig_c

                n += 1

                if abs(z + c) > 16:
                    break

            # Greyscale color based on 'n'
            # bright = [normalize(n, 0, 100, 0, 255) for x in range(3)]
            bright = [(n * 16) % 255 for i in range(3)]
            # Draw onto pixel
            pygame.draw.rect(surface, bright, (i, j, 1, 1))


def normalize(x, m0, m1, r0, r1):
    """
    Normalizes x which varies from the range [m0, m1] to the range [r0, r1]
    @params: int, int, int, int, int
    @return: float
    """
    return (r1 - r0) * ((x - m0) / (m1 - m0)) + r0


if __name__ == "__main__":
    # Run main program
    main()

