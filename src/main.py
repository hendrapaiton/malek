from dataclasses import dataclass

import flet as ft


@dataclass
class AppState:
    count: int

    def increment(self):
        self.count += 1


def main(page: ft.Page):
    state = AppState(count=0)

    text = ft.Text(value=f"{state.count}", size=50)

    def increment(e):
        state.increment()
        text.value = f"{state.count}"
        page.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                text,
                alignment=ft.Alignment.CENTER,
            ),
            expand=True,
        )
    )


ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)