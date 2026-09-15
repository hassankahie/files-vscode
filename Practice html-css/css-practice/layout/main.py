import tkinter as tk
import random
import threading
import time
import winsound


class EmergencyPrank:
    def __init__(self, root):

        self.root = root
        self.root.title("CRITICAL SECURITY ALERT")

        # ==========================================
        # FULL SCREEN
        # ==========================================

        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#050000")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        # ==========================================
        # CANVAS
        # ==========================================

        self.canvas = tk.Canvas(
            root,
            bg="#050000",
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        # ==========================================
        # VARIABLES
        # ==========================================

        self.running = True
        self.flash = False

        # ==========================================
        # ESC TO EXIT
        # ==========================================

        self.root.bind(
            "<Escape>",
            self.close
        )

        # ==========================================
        # START
        # ==========================================

        self.create_matrix()
        self.warning_screen()

        # Alarm
        threading.Thread(
            target=self.siren,
            daemon=True
        ).start()

        # Fake terminal
        self.fake_terminal()

        # Fake scanning
        self.root.after(
            1000,
            self.start_scan
        )

    # ==================================================
    # MATRIX BACKGROUND
    # ==================================================

    def create_matrix(self):

        characters = "0101010101010101"

        for _ in range(250):

            x = random.randint(
                0,
                self.width
            )

            y = random.randint(
                80,
                self.height
            )

            self.canvas.create_text(

                x,
                y,

                text=random.choice(
                    characters
                ),

                fill=random.choice([
                    "#180000",
                    "#220000",
                    "#2b0000",
                    "#330000"
                ]),

                font=(
                    "Consolas",
                    random.randint(
                        10,
                        18
                    )
                )
            )

    # ==================================================
    # RED FLASHING WARNING
    # ==================================================

    def warning_screen(self):

        if not self.running:
            return

        self.flash = not self.flash

        # Balanced flashing
        if self.flash:

            background = "#260000"
            red = "#ff0000"

        else:

            background = "#070000"
            red = "#8b0000"

        self.canvas.configure(
            bg=background
        )

        self.canvas.delete(
            "warning"
        )

        # ==========================================
        # OUTER BORDER
        # ==========================================

        self.canvas.create_rectangle(

            20,
            20,

            self.width - 20,
            self.height - 20,

            outline=red,

            width=7,

            tags="warning"
        )

        # ==========================================
        # TOP ALERT BAR
        # ==========================================

        self.canvas.create_rectangle(

            0,
            0,

            self.width,
            85,

            fill=red,

            outline="",

            tags="warning"
        )

        self.canvas.create_text(

            self.width // 2,
            42,

            text="⚠  CRITICAL SECURITY ALERT  ⚠",

            fill="white",

            font=(
                "Arial",
                32,
                "bold"
            ),

            tags="warning"
        )

        # ==========================================
        # WARNING ICON
        # ==========================================

        self.canvas.create_text(

            self.width // 2,
            160,

            text="⚠",

            fill=red,

            font=(
                "Arial",
                100,
                "bold"
            ),

            tags="warning"
        )

        # ==========================================
        # MAIN TITLE
        # ==========================================

        self.canvas.create_text(

            self.width // 2,
            275,

            text="SECURITY BREACH DETECTED",

            fill="white",

            font=(
                "Consolas",
                40,
                "bold"
            ),

            tags="warning"
        )

        # ==========================================
        # SECOND MESSAGE
        # ==========================================

        self.canvas.create_text(

            self.width // 2,
            335,

            text="UNAUTHORIZED ACCESS DETECTED",

            fill="#ff3333",

            font=(
                "Consolas",
                23,
                "bold"
            ),

            tags="warning"
        )

        # ==========================================
        # EMERGENCY PROTOCOL
        # ==========================================

        self.canvas.create_text(

            self.width // 2,
            390,

            text="EMERGENCY SECURITY PROTOCOL ACTIVATED",

            fill="#ff7777",

            font=(
                "Consolas",
                18
            ),

            tags="warning"
        )

        self.root.after(
            300,
            self.warning_screen
        )

    # ==================================================
    # BALANCED EMERGENCY SIREN
    # ==================================================

    def siren(self):

        while self.running:

            try:

                # ----------------------------------
                # RISING TONE
                # ----------------------------------

                winsound.Beep(
                    700,
                    180
                )

                winsound.Beep(
                    1000,
                    180
                )

                winsound.Beep(
                    1400,
                    220
                )

                time.sleep(
                    0.15
                )

                # ----------------------------------
                # FALLING TONE
                # ----------------------------------

                winsound.Beep(
                    1400,
                    220
                )

                winsound.Beep(
                    1000,
                    180
                )

                winsound.Beep(
                    700,
                    180
                )

                # Small pause
                time.sleep(
                    0.40
                )

            except Exception:
                break

    # ==================================================
    # FAKE TERMINAL
    # ==================================================

    def fake_terminal(self):

        if not self.running:
            return

        messages = [

            "[SECURITY] Monitoring network traffic...",

            "[FIREWALL] Suspicious connection detected.",

            "[AUTH] Unauthorized session detected.",

            "[SYSTEM] Emergency protocol activated.",

            "[NETWORK] Anomaly detected.",

            "[SCAN] Security analysis running...",

            "[ALERT] Critical event detected.",

            "[SYSTEM] Security lockdown simulation active.",

            "[NETWORK] Connection anomaly detected.",

            "[SECURITY] Threat analysis running.",

            "[CORE] System integrity check initiated.",

            "[ALERT] Multiple security events detected."

        ]

        message = random.choice(
            messages
        )

        self.canvas.create_text(

            random.randint(
                100,
                self.width - 100
            ),

            random.randint(
                470,
                self.height - 120
            ),

            text=message,

            fill=random.choice([
                "#ff2222",
                "#cc2222",
                "#990000"
            ]),

            font=(
                "Consolas",
                random.randint(
                    12,
                    16
                )
            ),

            anchor="w"
        )

        self.root.after(

            random.randint(
                180,
                450
            ),

            self.fake_terminal
        )

    # ==================================================
    # START FAKE SCAN
    # ==================================================

    def start_scan(self):

        if not self.running:
            return

        self.progress = 0

        # ==========================================
        # SCAN TEXT
        # ==========================================

        self.scan_text = self.canvas.create_text(

            self.width // 2,
            self.height - 150,

            text="SECURITY ANALYSIS: 0%",

            fill="#ff3333",

            font=(
                "Consolas",
                18,
                "bold"
            )
        )

        # ==========================================
        # PROGRESS BACKGROUND
        # ==========================================

        self.canvas.create_rectangle(

            self.width // 2 - 300,
            self.height - 110,

            self.width // 2 + 300,
            self.height - 75,

            outline="#660000",

            width=2
        )

        # ==========================================
        # PROGRESS BAR
        # ==========================================

        self.progress_bar = self.canvas.create_rectangle(

            self.width // 2 - 300,
            self.height - 110,

            self.width // 2 - 300,
            self.height - 75,

            fill="#ff0000",

            outline=""
        )

        self.update_scan()

    # ==================================================
    # UPDATE SCAN
    # ==================================================

    def update_scan(self):

        if not self.running:
            return

        if self.progress < 100:

            self.progress += random.randint(
                1,
                3
            )

            if self.progress > 100:
                self.progress = 100

            # Calculate width
            bar_width = (
                600
                * self.progress
                / 100
            )

            self.canvas.coords(

                self.progress_bar,

                self.width // 2 - 300,

                self.height - 110,

                self.width // 2 - 300
                + bar_width,

                self.height - 75
            )

            self.canvas.itemconfig(

                self.scan_text,

                text=f"SECURITY ANALYSIS: {self.progress}%"
            )

            self.root.after(

                100,

                self.update_scan
            )

        else:

            # Finish prank
            self.root.after(
                1800,
                self.prank_reveal
            )

    # ==================================================
    # PRANK REVEAL
    # ==================================================

    def prank_reveal(self):

        self.running = False

        self.canvas.delete(
            "all"
        )

        self.canvas.configure(
            bg="#050505"
        )

        # ==========================================
        # BIG PRANK MESSAGE
        # ==========================================

        self.canvas.create_text(

            self.width // 2,

            self.height // 2 - 100,

            text="😂 YOU GOT PRANKED!",

            fill="#00ff66",

            font=(
                "Arial",
                65,
                "bold"
            )
        )

        self.canvas.create_text(

            self.width // 2,

            self.height // 2,

            text="YOUR SYSTEM IS SAFE",

            fill="white",

            font=(
                "Arial",
                40,
                "bold"
            )
        )

        self.canvas.create_text(

            self.width // 2,

            self.height // 2 + 70,

            text="Nothing was hacked 😎",

            fill="#999999",

            font=(
                "Consolas",
                22
            )
        )

        self.canvas.create_text(

            self.width // 2,

            self.height // 2 + 140,

            text="Press ESC to exit",

            fill="#555555",

            font=(
                "Consolas",
                16
            )
        )

    # ==================================================
    # CLOSE
    # ==================================================

    def close(self, event=None):

        self.running = False

        self.root.destroy()


# ======================================================
# RUN APPLICATION
# ======================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = EmergencyPrank(
        root
    )

    root.mainloop()