import flet as ft


def chatbot_view(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Chatbot Page",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE,
                ),
                ft.Text("This is a simple chatbot interface.", size=16),
                ft.TextField(
                    label="Type your message...",
                    width=400,
                    border_radius=10,
                ),
                ft.ElevatedButton(
                    "Send",
                    width=100,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.BLUE,
                        color=ft.Colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                ),
                ft.ElevatedButton(
                    "Back to Register",
                    on_click=lambda e: page.go("/register"),
                    width=150,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.GREY,
                        color=ft.Colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.Alignment.CENTER,
        padding=20,
        bgcolor=ft.Colors.GREY_50,
        border_radius=15,
        width=500,
        height=400,
    )
