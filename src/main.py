import flet as ft
from views.register_page import register_view
from views.chatbot_page import chatbot_view


def main(page: ft.Page):
    page.title = "Multi-Page App"
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_change(e):
        page.views.clear()
        if page.route == "/register":
            page.views.append(
                ft.View(
                    "/register",
                    [
                        ft.AppBar(title=ft.Text("Register"), bgcolor=ft.Colors.BLUE),
                        ft.SafeArea(register_view(page), expand=True),
                    ],
                )
            )
        elif page.route == "/chatbot":
            page.views.append(
                ft.View(
                    "/chatbot",
                    [
                        ft.AppBar(title=ft.Text("Chatbot"), bgcolor=ft.Colors.BLUE),
                        ft.SafeArea(chatbot_view(page), expand=True),
                    ],
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/register")


ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)
