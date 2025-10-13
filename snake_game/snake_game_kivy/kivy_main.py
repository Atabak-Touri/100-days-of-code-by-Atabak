import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from snake_kivy import Snake
from food_kivy import Food
from scoreboard_kivey import Scoreboard

WINDOW_SIZE = 400
SEGMENT_SIZE = 20

DIRECTION_MAP = {
    'up': (0, 1),
    'down': (0, -1),
    'left': (-1, 0),
    'right': (1, 0)
}

class SnakeGameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.snake = Snake()
        self.food = Food(min_x=-180, max_x=180, min_y=-180, max_y=180)
        self.scoreboard = Scoreboard()
        self.game_over = False
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        if self._keyboard.widget:
            self._keyboard.widget.focus = True
        self._keyboard.bind(on_key_down=self._on_key_down)
        Clock.schedule_interval(self.update, 0.15)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        key = keycode[1]
        if key in DIRECTION_MAP:
            getattr(self.snake, key)()
        return True

    def update(self, dt):
        if self.game_over:
            return
        self.snake.move()
        # Check collision with food
        if self._distance(self.snake.head, self.food.position) < SEGMENT_SIZE:
            self.food.refresh()
            self.snake.extend()
            self.scoreboard.increase_score()
        # Check collision with wall
        x, y = self.snake.head
        if abs(x) > WINDOW_SIZE // 2 - SEGMENT_SIZE or abs(y) > WINDOW_SIZE // 2 - SEGMENT_SIZE:
            self.end_game()
        # Check collision with self
        for segment in self.snake.segments[1:]:
            if self._distance(self.snake.head, segment) < SEGMENT_SIZE // 2:
                self.end_game()
        self.canvas.clear()
        self.draw()

    def end_game(self):
        self.game_over = True
        self.scoreboard.game_over()
        self.canvas.clear()
        self.draw()

    def _distance(self, a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    def draw(self):
        with self.canvas:
            # Draw background
            Color(0, 0, 0)
            Rectangle(pos=(0, 0), size=(WINDOW_SIZE, WINDOW_SIZE))
            # Draw food
            Color(0, 1, 0)
            Rectangle(pos=(self.food.position[0] + WINDOW_SIZE // 2 - SEGMENT_SIZE // 2,
                           self.food.position[1] + WINDOW_SIZE // 2 - SEGMENT_SIZE // 2),
                      size=(SEGMENT_SIZE, SEGMENT_SIZE))
            # Draw snake
            Color(1, 1, 1)
            for segment in self.snake.segments:
                Rectangle(pos=(segment[0] + WINDOW_SIZE // 2 - SEGMENT_SIZE // 2,
                               segment[1] + WINDOW_SIZE // 2 - SEGMENT_SIZE // 2),
                          size=(SEGMENT_SIZE, SEGMENT_SIZE))
        # Draw score and game over text
        self._draw_labels()

    def _draw_labels(self):
        # Remove old labels
        self.clear_widgets()
        # Score label
        score_label = Label(text=f"Score: {self.scoreboard.score}",
                            pos=(0, WINDOW_SIZE // 2 - 30),
                            size_hint=(None, None),
                            color=(1, 1, 1, 1),
                            font_size=20)
        self.add_widget(score_label)
        if self.game_over:
            game_over_label = Label(text="GAME OVER",
                                    pos=(0, 0),
                                    size_hint=(None, None),
                                    color=(1, 0, 0, 1),
                                    font_size=40)
            self.add_widget(game_over_label)

class SnakeApp(App):
    def build(self):
        Window.size = (WINDOW_SIZE, WINDOW_SIZE)
        return SnakeGameWidget()

if __name__ == "__main__":
    SnakeApp().run()
