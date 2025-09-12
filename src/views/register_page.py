import flet as ft


def register_view(page: ft.Page):
    def on_register(e):
        username = username_field.value
        email = email_field.value
        password = password_field.value
        confirm_password = confirm_password_field.value

        if not username or not email or not password or not confirm_password:
            snack_bar = ft.SnackBar(ft.Text("All fields are required!"))
            page.snack_bar = snack_bar
            snack_bar.open = True
            page.update()
            return

        if password != confirm_password:
            snack_bar = ft.SnackBar(ft.Text("Passwords do not match!"))
            page.snack_bar = snack_bar
            snack_bar.open = True
            page.update()
            return

        # Here you can add logic to save the user, e.g., call an API or database
        snack_bar = ft.SnackBar(ft.Text(f"Registration successful for {username}!"))
        page.snack_bar = snack_bar
        snack_bar.open = True
        page.update()
        # Navigate to chatbot after successful registration
        page.go("/chatbot")

    name_field = ft.TextField(
        label="Fullname",
        width=300,
        prefix_icon=ft.Icons.PERSON,
        border_radius=10,
    )

    email_field = ft.TextField(
        label="Email",
        width=300,
        prefix_icon=ft.Icons.EMAIL,
        border_radius=10,
    )

    register_button = ft.ElevatedButton(
        "Register",
        on_click=on_register,
        width=300,
        height=50,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Create Account",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE,
                ),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                name_field,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                email_field,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                register_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.Alignment.CENTER,
        padding=20,
        bgcolor=ft.Colors.GREY_50,
        border_radius=15,
        width=400,
        height=500,
    )
