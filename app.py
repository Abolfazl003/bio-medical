# -*- coding: utf-8 -*-
"""
رابط کاربری اصلی اپلیکیشن آمادگی کنکور کارشناسی ارشد مهندسی پزشکی
"""

import os
import json
import random
from datetime import datetime
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

from data.subjects import SUBJECTS
from data.questions import QUESTION_BANK
from data.exams import EXAMS


APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROGRESS_FILE = os.path.join(APP_DIR, "user_progress.json")


# --- تم و قالب ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

COLORS = {
    "bg": "#0f172a",
    "card": "#1e293b",
    "card_hover": "#334155",
    "accent": "#38bdf8",
    "accent2": "#a78bfa",
    "success": "#22c55e",
    "danger": "#ef4444",
    "warning": "#f59e0b",
    "text": "#e2e8f0",
    "muted": "#94a3b8",
    "border": "#334155",
}


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"bookmarks": [], "saved_questions": [], "completed_lessons": [], "quiz_stats": {"correct":0,"total":0},
            "exam_results": [], "last_opened": None, "theme": "Dark"}


def save_progress(progress):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


class BMEEngineeringApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("اپلیکیشن آمادگی کنکور کارشناسی ارشد مهندسی پزشکی 🩺📚")
        self.geometry("1280x800")
        self.minsize(1000, 680)

        self.progress = load_progress()
        self.quiz_active = False
        self.quiz_q_index = 0
        self.quiz_correct = 0
        self.quiz_questions = []
        self.current_quiz_subject = None
        self.exam_active = False
        self.exam_q_index = 0
        self.exam_correct = 0
        self.exam_answers = []
        self.current_exam = None
        self.exam_timer = None
        self.exam_remaining = 0

        self._build_layout()
        self.show_dashboard()

    # ----------------------------------------------------------------
    # Layout
    # ----------------------------------------------------------------
    def _build_layout(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- سایدبار ---
        self.sidebar = ctk.CTkFrame(self, width=240, corner_radius=0, fg_color=COLORS["bg"])
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.grid_propagate(False)

        # عنوان
        title = ctk.CTkLabel(self.sidebar, text="مهندسی پزشکی\nارشد کنکور",
                             font=ctk.CTkFont("Vazirmatn", size=20, weight="bold"),
                             text_color=COLORS["accent"], justify="right")
        title.pack(pady=(24, 6), padx=20)

        subtitle = ctk.CTkLabel(self.sidebar, text="BME MSc Prep",
                                font=ctk.CTkFont(size=12), text_color=COLORS["muted"])
        subtitle.pack(pady=(0, 20))

        self._nav_btn("🏠  داشبورد", self.show_dashboard)
        self._nav_btn("📚  دروس و درس‌نامه", self.show_subjects)
        self._nav_btn("📝  بانک سوالات", self.show_quiz_home)
        self._nav_btn("🎓  آزمون‌های ۱۰ ساله", self.show_exams_home)
        self._nav_btn("📖  کتاب‌های مرجع", self.show_books)
        self._nav_btn("⭐  نشان‌شده‌ها", self.show_bookmarks)
        self._nav_btn("⚙️  تنظیمات", self.show_settings)

        # کارت آمار در پایین سایدبار
        stat_card = ctk.CTkFrame(self.sidebar, fg_color=COLORS["card"], corner_radius=12)
        stat_card.pack(side="bottom", fill="x", padx=16, pady=16)
        ctk.CTkLabel(stat_card, text="آمار کلی", font=ctk.CTkFont(size=14, weight="bold"),
                     text_color=COLORS["text"]).pack(pady=(12, 6))
        total = self.progress["quiz_stats"]["total"]
        correct = self.progress["quiz_stats"]["correct"]
        acc = (correct*100)//total if total else 0
        self.stat_label = ctk.CTkLabel(stat_card,
            text=f"سوالات پاسخ داده: {total}\nدرست: {correct}  ({acc}%)",
            font=ctk.CTkFont(size=12), text_color=COLORS["muted"], justify="right")
        self.stat_label.pack(pady=(0,12))

        # --- محتوای اصلی ---
        self.content = ctk.CTkFrame(self, fg_color="#0b1120", corner_radius=0)
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

    def _nav_btn(self, text, cmd):
        btn = ctk.CTkButton(self.sidebar, text=text, anchor="w",
                            fg_color="transparent", hover_color=COLORS["card_hover"],
                            text_color=COLORS["text"], font=ctk.CTkFont(size=14),
                            command=cmd, height=40, corner_radius=8)
        btn.pack(fill="x", padx=12, pady=3)
        return btn

    # ----------------------------------------------------------------
    # helpers
    # ----------------------------------------------------------------
    def clear_content(self):
        for w in self.content.winfo_children():
            w.destroy()

    def make_scroll(self, parent):
        scroll = ctk.CTkScrollableFrame(parent, fg_color="transparent",
                                        scrollbar_button_color=COLORS["border"],
                                        scrollbar_button_hover_color=COLORS["muted"])
        scroll.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)
        scroll.grid_columnconfigure(0, weight=1)
        return scroll

    def header(self, parent, title, subtitle=None):
        h = ctk.CTkFrame(parent, fg_color="transparent")
        h.pack(fill="x", pady=(0, 20))
        ctk.CTkLabel(h, text=title, font=ctk.CTkFont(size=28, weight="bold"),
                     text_color=COLORS["text"]).pack(anchor="w")
        if subtitle:
            ctk.CTkLabel(h, text=subtitle, font=ctk.CTkFont(size=14),
                         text_color=COLORS["muted"]).pack(anchor="w", pady=(4,0))

    # ----------------------------------------------------------------
    # DASHBOARD
    # ----------------------------------------------------------------
    def show_dashboard(self):
        self.clear_content()
        scroll = self.make_scroll(self.content)
        self.header(scroll, "سلام! به اپلیکیشن آمادگی کنکور خوش آمدی 👋",
                    "مطالعه درس‌نامه، تست‌زنی و شرکت در آزمون‌های ۱۰ ساله مهندسی پزشکی")

        # سه کارت آمار
        row = ctk.CTkFrame(scroll, fg_color="transparent")
        row.pack(fill="x", pady=10)
        row.grid_columnconfigure((0,1,2), weight=1)

        total_q = sum(len(v) for v in QUESTION_BANK.values())
        lessons_count = sum(len(s["lessons"]) for s in SUBJECTS)
        total = self.progress["quiz_stats"]["total"]
        correct = self.progress["quiz_stats"]["correct"]
        acc = int((correct*100)/total) if total else 0

        self.stat_card(row, f"{lessons_count}", "تعداد درس‌نامه 📖", COLORS["accent"], 0, 0)
        self.stat_card(row, f"{total_q}+", "سوال تستی 📝", COLORS["accent2"], 0, 1)
        self.stat_card(row, f"{acc}%", "درصد پاسخ صحیح ✅", COLORS["success"], 0, 2)

        # دکمه‌های شروع سریع
        ctk.CTkLabel(scroll, text="شروع سریع", font=ctk.CTkFont(size=18, weight="bold"),
                     text_color=COLORS["text"]).pack(anchor="w", pady=(20,10))
        quick = ctk.CTkFrame(scroll, fg_color="transparent")
        quick.pack(fill="x")
        quick.grid_columnconfigure((0,1,2), weight=1)
        self.action_card(quick, "🎲", "تست تصادفی", "یک دور سوال ترکیبی از همه دروس",
                         lambda: self.start_quiz(None), 0, 0, COLORS["accent"])
        self.action_card(quick, "🎓", "آزمون جامع", "شروع آزمون سال اخیر",
                         lambda: self.start_exam(EXAMS[-1]), 0, 1, COLORS["accent2"])
        self.action_card(quick, "📚", "مطالعه درس‌نامه", "انتخاب درس برای مطالعه",
                         self.show_subjects, 0, 2, COLORS["success"])

        # دروس
        ctk.CTkLabel(scroll, text="دروس موجود", font=ctk.CTkFont(size=18, weight="bold"),
                     text_color=COLORS["text"]).pack(anchor="w", pady=(24,10))
        sub_grid = ctk.CTkFrame(scroll, fg_color="transparent")
        sub_grid.pack(fill="x")
        sub_grid.grid_columnconfigure((0,1,2), weight=1)
        for i, s in enumerate(SUBJECTS):
            r, c = divmod(i, 3)
            q_count = len(QUESTION_BANK.get(s["id"], []))
            l_count = len(s["lessons"])
            self.subject_card(sub_grid, s, q_count, l_count, r, c)

        # نتیجه آخرین آزمون
        if self.progress["exam_results"]:
            last = self.progress["exam_results"][-1]
            ctk.CTkLabel(scroll, text="آخرین نتیجه آزمون", font=ctk.CTkFont(size=18, weight="bold"),
                         text_color=COLORS["text"]).pack(anchor="w", pady=(24,10))
            card = ctk.CTkFrame(scroll, fg_color=COLORS["card"], corner_radius=14)
            card.pack(fill="x")
            pct = int(last["score"]*100/last["total"])
            ctk.CTkLabel(card, text=f"دوره {last['year']}  —  {last['score']} از {last['total']}  ({pct}%)",
                         font=ctk.CTkFont(size=16, weight="bold"),
                         text_color=COLORS["warning"]).pack(pady=16, padx=20, anchor="w")

    def stat_card(self, parent, big, label, color, r, c):
        card = ctk.CTkFrame(parent, fg_color=COLORS["card"], corner_radius=14)
        card.grid(row=r, column=c, sticky="nsew", padx=6, pady=6, ipady=16)
        ctk.CTkLabel(card, text=big, font=ctk.CTkFont(size=30, weight="bold"), text_color=color).pack(pady=(12,0))
        ctk.CTkLabel(card, text=label, font=ctk.CTkFont(size=12), text_color=COLORS["muted"]).pack(pady=(0,10))

    def action_card(self, parent, emoji, title, desc, cmd, r, c, color):
        card = ctk.CTkFrame(parent, fg_color=COLORS["card"], corner_radius=14, cursor="hand2")
        card.grid(row=r, column=c, sticky="nsew", padx=6, pady=6, ipady=20)
        card.bind("<Button-1>", lambda e: cmd())
        for w in card.winfo_children():
            w.bind("<Button-1>", lambda e: cmd())
        ctk.CTkLabel(card, text=emoji, font=ctk.CTkFont(size=36), text_color=color).pack(pady=(10,0))
        tl = ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=15, weight="bold"), text_color=COLORS["text"])
        tl.pack(pady=(6,2))
        ctk.CTkLabel(card, text=desc, font=ctk.CTkFont(size=11), text_color=COLORS["muted"], justify="right",
                     wraplength=220).pack(padx=16)
        ctk.CTkButton(card, text="شروع", command=cmd, fg_color=color, hover_color=color,
                      text_color="#0f172a", font=ctk.CTkFont(weight="bold"),
                      width=120, height=30, corner_radius=8).pack(pady=12)

    def subject_card(self, parent, s, q_count, l_count, r, c):
        card = ctk.CTkFrame(parent, fg_color=COLORS["card"], corner_radius=14, cursor="hand2")
        card.grid(row=r, column=c, sticky="nsew", padx=6, pady=6, ipady=16)
        card.bind("<Button-1>", lambda e, sid=s["id"]: self.show_subject_detail(sid))
        for child in card.winfo_children():
            child.bind("<Button-1>", lambda e, sid=s["id"]: self.show_subject_detail(sid))
        ctk.CTkLabel(card, text=s["emoji"], font=ctk.CTkFont(size=32)).pack(pady=(10,0))
        ctk.CTkLabel(card, text=s["name"], font=ctk.CTkFont(size=13, weight="bold"),
                     text_color=COLORS["text"], wraplength=260, justify="right").pack(pady=(6,2), padx=10)
        ctk.CTkLabel(card, text=f"{l_count} فصل  •  {q_count} سوال",
                     font=ctk.CTkFont(size=11), text_color=COLORS["muted"]).pack()
        btn_bar = ctk.CTkFrame(card, fg_color="transparent")
        btn_bar.pack(pady=(8,10))
        ctk.CTkButton(btn_bar, text="📖 مطالعه", width=80, height=28, fg_color=s["color"], hover_color=s["color"],
                      text_color="white", font=ctk.CTkFont(size=11),
                      command=lambda sid=s["id"]: self.show_subject_detail(sid)).pack(side="right", padx=3)
        ctk.CTkButton(btn_bar, text="📝 تست", width=80, height=28, fg_color=COLORS["card_hover"],
                      hover_color=COLORS["border"], text_color=COLORS["text"], font=ctk.CTkFont(size=11),
                      command=lambda sid=s["id"]: self.start_quiz(sid)).pack(side="right", padx=3)

    # ----------------------------------------------------------------
    # SUBJECTS LIST
    # ----------------------------------------------------------------
    def show_subjects(self):
        self.clear_content()
        scroll = self.make_scroll(self.content)
        self.header(scroll, "📚 دروس و سرفصل‌ها", "یک درس را انتخاب کنید تا درس‌نامه و سوالات را ببینید")
        grid = ctk.CTkFrame(scroll, fg_color="transparent")
        grid.pack(fill="x")
        grid.grid_columnconfigure((0,1,2), weight=1)
        for i, s in enumerate(SUBJECTS):
            r, c = divmod(i, 3)
            self.subject_card(grid, s, len(QUESTION_BANK.get(s["id"],[])), len(s["lessons"]), r, c)

    def show_subject_detail(self, subject_id):
        sub = next(s for s in SUBJECTS if s["id"]==subject_id)
        self.clear_content()
        scroll = self.make_scroll(self.content)

        top = ctk.CTkFrame(scroll, fg_color=COLORS["card"], corner_radius=14)
        top.pack(fill="x", pady=(0,20))
        top.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(top, text=sub["emoji"], font=ctk.CTkFont(size=48)).grid(row=0, column=0, padx=20, pady=20, rowspan=2)
        ctk.CTkLabel(top, text=sub["name"], font=ctk.CTkFont(size=22, weight="bold"),
                     text_color=COLORS["text"], anchor="w", justify="right").grid(row=0, column=1, sticky="w")
        ctk.CTkLabel(top, text=f"{len(sub['lessons'])} فصل  •  {len(QUESTION_BANK.get(subject_id,[]))} سوال تستی",
                     font=ctk.CTkFont(size=12), text_color=COLORS["muted"], anchor="w").grid(row=1, column=1, sticky="w")
        btns = ctk.CTkFrame(top, fg_color="transparent")
        btns.grid(row=0, column=2, rowspan=2, padx=20)
        ctk.CTkButton(btns, text="📝 شروع تست این درس", command=lambda sid=subject_id: self.start_quiz(sid),
                      fg_color=sub["color"], hover_color=sub["color"], text_color="white",
                      width=180, height=40, corner_radius=10,
                      font=ctk.CTkFont(weight="bold")).pack(pady=4)
        ctk.CTkButton(btns, text="🔙 بازگشت به دروس", command=self.show_subjects,
                      fg_color=COLORS["card_hover"], hover_color=COLORS["border"],
                      text_color=COLORS["text"], width=180, height=34, corner_radius=10).pack(pady=4)

        ctk.CTkLabel(scroll, text="📖 سرفصل‌ها و درس‌نامه", font=ctk.CTkFont(size=18, weight="bold"),
                     text_color=COLORS["text"]).pack(anchor="w", pady=(10,10))

        for idx, lesson in enumerate(sub["lessons"], 1):
            completed = f"{subject_id}__{idx}" in self.progress["completed_lessons"]
            self.lesson_card(scroll, sub, idx, lesson, completed)

    def lesson_card(self, parent, sub, idx, lesson, completed):
        card = ctk.CTkFrame(parent, fg_color=COLORS["card"], corner_radius=12)
        card.pack(fill="x", pady=6)
        card.grid_columnconfigure(0, weight=1)

        head = ctk.CTkFrame(card, fg_color="transparent")
        head.pack(fill="x", padx=16, pady=10)
        head.grid_columnconfigure(1, weight=1)

        num = ctk.CTkLabel(head, text=f"{idx:02d}", font=ctk.CTkFont(size=16, weight="bold"),
                           fg_color=sub["color"], text_color="white", width=36, height=36, corner_radius=18)
        num.grid(row=0, column=0, padx=(0,12))
        ctk.CTkLabel(head, text=lesson["title"], font=ctk.CTkFont(size=16, weight="bold"),
                     text_color=COLORS["text"], anchor="w").grid(row=0, column=1, sticky="w")

        if completed:
            ctk.CTkLabel(head, text="✅ خوانده شد", font=ctk.CTkFont(size=11),
                         text_color=COLORS["success"]).grid(row=0, column=2, padx=10)

        body = ctk.CTkTextbox(card, fg_color="#0f172a", text_color=COLORS["text"],
                              font=ctk.CTkFont(family="Tahoma", size=13), wrap="word",
                              corner_radius=8, height=260, pad=12)
        body.pack(fill="x", padx=16, pady=(0,8))
        body.insert("1.0", lesson["content"])
        body.configure(state="disabled")
        # RTL alignment
        body.tag_config("rtl", justify="right")
        try:
            body.tag_add("rtl", "1.0", "end")
        except Exception:
            pass

        ftr = ctk.CTkFrame(card, fg_color="transparent")
        ftr.pack(fill="x", padx=16, pady=(0,12))
        key = f"{sub['id']}__{idx}"
        def toggle_complete(k=key):
            if k in self.progress["completed_lessons"]:
                self.progress["completed_lessons"].remove(k)
            else:
                self.progress["completed_lessons"].append(k)
            save_progress(self.progress)
            self.show_subject_detail(sub["id"])
        lbl = "✅ مطالعه‌شده" if completed else "⬜ علامت‌گذاری به عنوان خوانده شده"
        ctk.CTkButton(ftr, text=lbl, command=toggle_complete,
                      fg_color=COLORS["success"] if completed else COLORS["card_hover"],
                      hover_color=COLORS["success"] if completed else COLORS["border"],
                      text_color="white", width=220, height=32, corner_radius=8).pack(side="right")

        def toggle_bookmark(title=lesson["title"], content=lesson["content"], sid=sub["id"]):
            bm = {"type":"lesson","subject":sid,"title":title,"content":content}
            # simple dedup by title
            for b in self.progress["bookmarks"]:
                if b.get("title")==title:
                    self.progress["bookmarks"].remove(b)
                    save_progress(self.progress)
                    self.show_subject_detail(sid)
                    return
            self.progress["bookmarks"].append(bm)
            save_progress(self.progress)
            messagebox.showinfo("نشان شد", "این فصل به نشان‌شده‌ها اضافه شد ⭐")
        already_bm = any(b.get("title")==lesson["title"] for b in self.progress["bookmarks"])
        ctk.CTkButton(ftr, text=("⭐ نشان شده" if already_bm else "☆ نشان کردن"),
                      command=toggle_bookmark,
                      fg_color=COLORS["warning"] if already_bm else COLORS["card_hover"],
                      hover_color=COLORS["warning"] if already_bm else COLORS["border"],
                      text_color="white", width=140, height=32, corner_radius=8).pack(side="right", padx=6)

    # ----------------------------------------------------------------
    # QUIZ
    # ----------------------------------------------------------------
    def show_quiz_home(self):
        self.clear_content()
        scroll = self.make_scroll(self.content)
        self.header(scroll, "📝 بانک سوالات", "یکی از دروس را برای تست‌زنی انتخاب کن یا تست تصادفی از همه دروس بزن")

        grid = ctk.CTkFrame(scroll, fg_color="transparent")
        grid.pack(fill="x", pady=10)
        grid.grid_columnconfigure((0,1,2), weight=1)

        # کارت ویژه آزمون تصادفی
        self.action_card(grid, "🎲", "تست تصادفی ترکیبی", "20 سوال از تمام دروس",
                         lambda: self.start_quiz(None), 0, 0, COLORS["accent"])

        for i, s in enumerate(SUBJECTS):
            r, c = divmod(i+1, 3)
            qc = len(QUESTION_BANK.get(s["id"], []))
            card = ctk.CTkFrame(grid, fg_color=COLORS["card"], corner_radius=14, cursor="hand2")
            card.grid(row=r, column=c, sticky="nsew", padx=6, pady=6, ipady=16)
            ctk.CTkLabel(card, text=s["emoji"], font=ctk.CTkFont(size=32)).pack(pady=(10,0))
            ctk.CTkLabel(card, text=s["name"], font=ctk.CTkFont(size=13, weight="bold"),
                         text_color=COLORS["text"], wraplength=240, justify="right").pack(pady=(6,2), padx=10)
            ctk.CTkLabel(card, text=f"{qc} سوال", font=ctk.CTkFont(size=11),
                         text_color=COLORS["muted"]).pack()
            ctk.CTkButton(card, text="شروع تست", command=lambda sid=s["id"]: self.start_quiz(sid),
                          fg_color=s["color"], hover_color=s["color"], text_color="white",
                          width=120, height=32, corner_radius=8,
                          font=ctk.CTkFont(weight="bold")).pack(pady=12)

    def start_quiz(self, subject_id=None):
        if subject_id is None:
            pool = []
            for sid, qs in QUESTION_BANK.items():
                for q in qs:
                    q = dict(q); q["subject"] = sid
                    pool.append(q)
            random.shuffle(pool)
            self.quiz_questions = pool[:20]
            self.current_quiz_subject = "ترکیبی"
        else:
            pool = []
            for q in QUESTION_BANK[subject_id]:
                q = dict(q); q["subject"] = subject_id
                pool.append(q)
            random.shuffle(pool)
            self.quiz_questions = pool[:min(len(pool), 20)]
            self.current_quiz_subject = next(s["name"] for s in SUBJECTS if s["id"]==subject_id)
        self.quiz_q_index = 0
        self.quiz_correct = 0
        self.quiz_active = True
        self.current_selected_answer = None
        self.render_quiz_question()

    def render_quiz_question(self):
        self.clear_content()
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        wrap = ctk.CTkFrame(self.content, fg_color="transparent")
        wrap.grid(row=0, column=0, sticky="nsew", padx=60, pady=40)
        wrap.grid_columnconfigure(0, weight=1)

        q = self.quiz_questions[self.quiz_q_index]
        total = len(self.quiz_questions)
        idx = self.quiz_q_index+1
        # پیشرفت
        prog_row = ctk.CTkFrame(wrap, fg_color="transparent")
        prog_row.pack(fill="x")
        ctk.CTkLabel(prog_row, text=f"سوال {idx} از {total} — {self.current_quiz_subject}",
                     font=ctk.CTkFont(size=14, weight="bold"), text_color=COLORS["accent"]).pack(side="right")
        pbar = ctk.CTkProgressBar(wrap, fg_color=COLORS["card"], progress_color=COLORS["accent"], height=8)
        pbar.pack(fill="x", pady=(6,20))
        pbar.set(idx/total)

        card = ctk.CTkFrame(wrap, fg_color=COLORS["card"], corner_radius=14)
        card.pack(fill="x")
        ctk.CTkLabel(card, text=q["q"], font=ctk.CTkFont(size=17, weight="bold"),
                     text_color=COLORS["text"], wraplength=800, justify="right").pack(padx=24, pady=22)

        self.current_selected_answer = tk.IntVar(value=-1)
        choices_frame = ctk.CTkFrame(card, fg_color="transparent")
        choices_frame.pack(fill="x", padx=24, pady=(0,10))
        letters = ["الف", "ب", "ج", "د"]
        for ci, choice in enumerate(q["choices"]):
            rb = ctk.CTkRadioButton(choices_frame, text=f"{letters[ci]})  {choice}",
                                    variable=self.current_selected_answer, value=ci,
                                    font=ctk.CTkFont(size=14), text_color=COLORS["text"],
                                    fg_color=COLORS["accent"], hover_color=COLORS["accent2"],
                                    command=self._set_colors_default)
            rb.pack(anchor="w", pady=8)

        self._answer_feedback = ctk.CTkLabel(wrap, text="", font=ctk.CTkFont(size=13), justify="right")
        self._answer_feedback.pack(pady=10, padx=24, anchor="e")

        btn_row = ctk.CTkFrame(wrap, fg_color="transparent")
        btn_row.pack(fill="x", pady=10)
        self._check_btn = ctk.CTkButton(btn_row, text="✅ ثبت پاسخ", command=self.check_quiz_answer,
                                        fg_color=COLORS["success"], hover_color="#16a34a",
                                        text_color="white", width=160, height=40, corner_radius=10,
                                        font=ctk.CTkFont(weight="bold"))
        self._check_btn.pack(side="left")
        self._next_btn = ctk.CTkButton(btn_row, text="بعدی ➡️", command=self.next_quiz_question,
                                       fg_color=COLORS["accent"], hover_color="#0ea5e9",
                                       text_color="#0f172a", width=140, height=40, corner_radius=10,
                                       font=ctk.CTkFont(weight="bold"), state="disabled")
        self._next_btn.pack(side="right")
        ctk.CTkButton(btn_row, text="🔙 انصراف", command=self.show_quiz_home,
                      fg_color=COLORS["card_hover"], hover_color=COLORS["border"],
                      text_color=COLORS["text"], width=100, height=40, corner_radius=10).pack(side="right", padx=6)

    def _set_colors_default(self):
        pass

    def check_quiz_answer(self):
        if self.current_selected_answer.get() == -1:
            messagebox.showinfo("انتخاب کنید", "لطفاً یک گزینه را انتخاب کنید.")
            return
        q = self.quiz_questions[self.quiz_q_index]
        chosen = self.current_selected_answer.get()
        self.progress["quiz_stats"]["total"] += 1
        if chosen == q["answer"]:
            self.quiz_correct += 1
            self.progress["quiz_stats"]["correct"] += 1
            text = "✅ پاسخ صحیح بود!\n\n🎯 راه حل کنکوری:\n" + q.get("konkori","") + "\n\n📚 توضیح کامل:\n" + q.get("full_solution","")
            self._answer_feedback.configure(text=text, text_color=COLORS["success"])
        else:
            correct_letter = ["الف","ب","ج","د"][q["answer"]]
            text = f"❌ پاسخ اشتباه! گزینه صحیح {correct_letter} بود.\n\n🎯 راه حل کنکوری:\n" + q.get("konkori","") + "\n\n📚 توضیح کامل:\n" + q.get("full_solution","")
            self._answer_feedback.configure(text=text, text_color=COLORS["danger"])
        save_progress(self.progress)
        self._check_btn.configure(state="disabled")
        self._next_btn.configure(state="normal")

    def next_quiz_question(self):
        self.quiz_q_index += 1
        if self.quiz_q_index >= len(self.quiz_questions):
            self.finish_quiz()
        else:
            self.render_quiz_question()

    def finish_quiz(self):
        self.quiz_active = False
        total = len(self.quiz_questions)
        pct = int(self.quiz_correct*100/total)
        self.clear_content()
        wrap = ctk.CTkFrame(self.content, fg_color="transparent")
        wrap.grid(row=0, column=0, sticky="nsew", padx=60, pady=60)
        ctk.CTkLabel(wrap, text="🎉 پایان تست", font=ctk.CTkFont(size=32, weight="bold"),
                     text_color=COLORS["accent"]).pack(pady=10)
        ctk.CTkLabel(wrap, text=f"{self.quiz_correct} درست از {total} سوال  —  {pct}%",
                     font=ctk.CTkFont(size=24), text_color=COLORS["text"]).pack(pady=10)
        msg = "عالی بود! 👏" if pct>=75 else ("خوب بود، بیشتر تمرین کن 💪" if pct>=50 else "لازم است درس‌نامه را مرور کنی 📖")
        ctk.CTkLabel(wrap, text=msg, font=ctk.CTkFont(size=16), text_color=COLORS["muted"]).pack(pady=8)

        btns = ctk.CTkFrame(wrap, fg_color="transparent")
        btns.pack(pady=30)
        ctk.CTkButton(btns, text="🔁 تست مجدد", command=lambda: self.start_quiz(None if self.current_quiz_subject=="ترکیبی" else self._current_sid()),
                      fg_color=COLORS["accent"], hover_color="#0ea5e9",
                      text_color="#0f172a", width=140, height=40, corner_radius=10,
                      font=ctk.CTkFont(weight="bold")).pack(side="right", padx=6)
        ctk.CTkButton(btns, text="🏠 داشبورد", command=self.show_dashboard,
                      fg_color=COLORS["card_hover"], hover_color=COLORS["border"],
                      text_color=COLORS["text"], width=140, height=40, corner_radius=10).pack(side="right", padx=6)

    def _current_sid(self):
        for s in SUBJECTS:
            if s["name"] == self.current_quiz_subject:
                return s["id"]
        return None

    # ----------------------------------------------------------------
    # EXAMS (10 years)
    # ----------------------------------------------------------------
    def show_exams_home(self):
        self.clear_content()
        scroll = self.make_scroll(self.content)
        self.header(scroll, "🎓 آزمون‌های ۱۰ سال اخیر کنکور ارشد مهندسی پزشکی",
                    "یک دوره را انتخاب و در زمان ۶۰ دقیقه به ۲۵ سوال پاسخ بده")
        grid = ctk.CTkFrame(scroll, fg_color="transparent")
        grid.pack(fill="x")
        grid.grid_columnconfigure((0,1,2), weight=1)
        for i, exam in enumerate(EXAMS):
            r, c = divmod(i, 3)
            prev = None
            for res in self.progress["exam_results"]:
                if res["year"]==exam["year"]:
                    prev = res
            self.exam_card(grid, exam, prev, r, c)

    def exam_card(self, parent, exam, prev, r, c):
        card = ctk.CTkFrame(parent, fg_color=COLORS["card"], corner_radius=14, cursor="hand2")
        card.grid(row=r, column=c, sticky="nsew", padx=6, pady=6, ipady=18)
        ctk.CTkLabel(card, text=f"📅", font=ctk.CTkFont(size=36)).pack(pady=(10,0))
        ctk.CTkLabel(card, text=f"دوره {exam['year']}", font=ctk.CTkFont(size=18, weight="bold"),
                     text_color=COLORS["text"]).pack(pady=(8,2))
        ctk.CTkLabel(card, text=f"{len(exam['questions'])} سوال  •  ۶۰ دقیقه",
                     font=ctk.CTkFont(size=11), text_color=COLORS["muted"]).pack()
        if prev:
            pct = int(prev["score"]*100/prev["total"])
            ctk.CTkLabel(card, text=f"آخرین نتیجه: {pct}%",
                         font=ctk.CTkFont(size=11, weight="bold"), text_color=COLORS["success"]).pack(pady=4)
        ctk.CTkButton(card, text="شروع آزمون", command=lambda e=exam: self.start_exam(e),
                      fg_color=COLORS["accent2"], hover_color=COLORS["accent2"],
                      text_color="white", width=140, height=34, corner_radius=8,
                      font=ctk.CTkFont(weight="bold")).pack(pady=12)

    def start_exam(self, exam):
        self.current_exam = exam
        self.exam_q_index = 0
        self.exam_correct = 0
        self.exam_answers = [-1]*len(exam["questions"])
        self.exam_active = True
        self.exam_remaining = 60*60   # 60 minutes in seconds
        self.render_exam_question()
        self._tick_exam_timer()

    def _tick_exam_timer(self):
        if not self.exam_active:
            return
        if self.exam_remaining <= 0:
            messagebox.showinfo("زمان تمام شد", "زمان آزمون تمام شد!")
            self.finish_exam()
            return
        m, s = divmod(self.exam_remaining, 60)
        if hasattr(self, "_timer_lbl") and self._timer_lbl.winfo_exists():
            self._timer_lbl.configure(text=f"⏱️  زمان باقی‌مانده: {m:02d}:{s:02d}")
        self.exam_remaining -= 1
        self.exam_timer = self.after(1000, self._tick_exam_timer)

    def render_exam_question(self):
        self.clear_content()
        self.content.grid_columnconfigure(0, weight=1)
        wrap = ctk.CTkFrame(self.content, fg_color="transparent")
        wrap.grid(row=0, column=0, sticky="nsew", padx=40, pady=30)
        wrap.grid_columnconfigure(0, weight=1)

        exam = self.current_exam
        q = exam["questions"][self.exam_q_index]
        total = len(exam["questions"])
        idx = self.exam_q_index+1

        top = ctk.CTkFrame(wrap, fg_color="transparent")
        top.pack(fill="x")
        ctk.CTkLabel(top, text=f"دوره {exam['year']}  •  سوال {idx} از {total}",
                     font=ctk.CTkFont(size=14, weight="bold"), text_color=COLORS["accent2"]).pack(side="right")
        self._timer_lbl = ctk.CTkLabel(top, text="⏱️  60:00", font=ctk.CTkFont(size=14, weight="bold"),
                                       text_color=COLORS["warning"])
        self._timer_lbl.pack(side="left")

        pbar = ctk.CTkProgressBar(wrap, fg_color=COLORS["card"], progress_color=COLORS["accent2"], height=8)
        pbar.pack(fill="x", pady=(6,20))
        pbar.set(idx/total)

        # نوار ناوبری سوالات
        nav = ctk.CTkScrollableFrame(wrap, fg_color=COLORS["card"], height=60,
                                    orientation="horizontal", corner_radius=10)
        nav.pack(fill="x", pady=(0,10))
        for qi in range(total):
            ans = self.exam_answers[qi]
            if qi == self.exam_q_index:
                col = COLORS["accent2"]; txt = "white"
            elif ans != -1:
                col = COLORS["success"]; txt = "white"
            else:
                col = COLORS["card_hover"]; txt = COLORS["text"]
            b = ctk.CTkButton(nav, text=f"{qi+1}", width=32, height=32, fg_color=col, text_color=txt,
                              corner_radius=16, font=ctk.CTkFont(weight="bold"),
                              command=lambda i=qi: self.jump_exam_question(i))
            b.pack(side="right", padx=3, pady=8)

        card = ctk.CTkFrame(wrap, fg_color=COLORS["card"], corner_radius=14)
        card.pack(fill="x", pady=10)
        ctk.CTkLabel(card, text=q["q"], font=ctk.CTkFont(size=17, weight="bold"),
                     text_color=COLORS["text"], wraplength=900, justify="right").pack(padx=24, pady=22)

        self._exam_choice_var = tk.IntVar(value=self.exam_answers[self.exam_q_index])
        choices_frame = ctk.CTkFrame(card, fg_color="transparent")
        choices_frame.pack(fill="x", padx=24, pady=(0,14))
        letters = ["الف","ب","ج","د"]
        for ci, choice in enumerate(q["choices"]):
            ctk.CTkRadioButton(choices_frame, text=f"{letters[ci]})  {choice}",
                               variable=self._exam_choice_var, value=ci,
                               font=ctk.CTkFont(size=14), text_color=COLORS["text"],
                               fg_color=COLORS["accent2"], hover_color=COLORS["accent"]).pack(anchor="w", pady=8)

        btn_row = ctk.CTkFrame(wrap, fg_color="transparent")
        btn_row.pack(fill="x", pady=10)
        ctk.CTkButton(btn_row, text="پایان آزمون", command=self.finish_exam,
                      fg_color=COLORS["danger"], hover_color="#dc2626",
                      text_color="white", width=120, height=36, corner_radius=8,
                      font=ctk.CTkFont(weight="bold")).pack(side="left")
        if idx < total:
            ctk.CTkButton(btn_row, text="بعدی ➡️", command=self.next_exam_question,
                          fg_color=COLORS["accent2"], hover_color=COLORS["accent"],
                          text_color="white", width=120, height=36, corner_radius=8,
                          font=ctk.CTkFont(weight="bold")).pack(side="right")
        else:
            ctk.CTkButton(btn_row, text="✅ ثبت و پایان آزمون", command=self.finish_exam,
                          fg_color=COLORS["success"], hover_color="#16a34a",
                          text_color="white", width=180, height=38, corner_radius=8,
                          font=ctk.CTkFont(weight="bold")).pack(side="right")
        if idx > 1:
            ctk.CTkButton(btn_row, text="⬅️ قبلی", command=self.prev_exam_question,
                          fg_color=COLORS["card_hover"], hover_color=COLORS["border"],
                          text_color=COLORS["text"], width=100, height=36, corner_radius=8).pack(side="right", padx=6)

    def jump_exam_question(self, i):
        # ذخیره پاسخ فعلی
        self.exam_answers[self.exam_q_index] = self._exam_choice_var.get()
        self.exam_q_index = i
        self.render_exam_question()

    def next_exam_question(self):
        self.exam_answers[self.exam_q_index] = self._exam_choice_var.get()
        self.exam_q_index += 1
        self.render_exam_question()

    def prev_exam_question(self):
        self.exam_answers[self.exam_q_index] = self._exam_choice_var.get()
        self.exam_q_index -= 1
        self.render_exam_question()

    def finish_exam(self):
        self.exam_active = False
        if self.exam_timer is not None:
            try: self.after_cancel(self.exam_timer)
            except Exception: pass
        # ذخیره پاسخ فعلی
        try:
            self.exam_answers[self.exam_q_index] = self._exam_choice_var.get()
        except Exception:
            pass
        # تصحیح
        correct = 0
        results = []
        for i, q in enumerate(self.current_exam["questions"]):
            chosen = self.exam_answers[i]
            if chosen == q["answer"]:
                correct += 1
            results.append({"chosen":chosen, "correct":q["answer"], "question":q["q"],
                            "choices":q["choices"], "explanation":q.get("explanation","")})
        total = len(self.current_exam["questions"])
        pct = int(correct*100/total)
        self.progress["exam_results"].append({
            "year": self.current_exam["year"], "score": correct, "total": total,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "details": results
        })
        save_progress(self.progress)

        # نمایش کارنامه
        self.clear_content()
        scroll = self.make_scroll(self.content)
        self.header(scroll, f"🎓 کارنامه آزمون دوره {self.current_exam['year']}",
                    f"{correct} درست از {total} سوال  —  درصد {pct}%  •  زمان باقی‌مانده: {self.exam_remaining//60} دقیقه")

        msg = "ممتاز! 🏆" if pct>=80 else ("خوب! 💪" if pct>=60 else ("نیاز به مطالعه بیشتر 📚" if pct>=40 else "بیشتر تلاش کن 🎯"))
        ctk.CTkLabel(scroll, text=msg, font=ctk.CTkFont(size=18, weight="bold"),
                     text_color=COLORS["warning"]).pack(anchor="w", pady=(0,20))

        for i, r in enumerate(results, 1):
            is_correct = r["chosen"] == r["correct"]
            card = ctk.CTkFrame(scroll, fg_color=COLORS["card"], corner_radius=10)
            card.pack(fill="x", pady=4)
            ctk.CTkLabel(card, text=f"سوال {i}  {'✅' if is_correct else '❌'}",
                         font=ctk.CTkFont(size=13, weight="bold"),
                         text_color=(COLORS["success"] if is_correct else COLORS["danger"])).pack(anchor="w", padx=14, pady=(10,0))
            ctk.CTkLabel(card, text=r["question"], font=ctk.CTkFont(size=13),
                         text_color=COLORS["text"], justify="right", wraplength=900).pack(anchor="w", padx=14, pady=4)
            letters=["الف","ب","ج","د"]
            ans_text = f"پاسخ شما: {letters[r['chosen']] if 0<=r['chosen']<4 else 'بدون پاسخ'}"
            cor_text = f" — پاسخ صحیح: {letters[r['correct']]}"
            ctk.CTkLabel(card, text=ans_text+cor_text, font=ctk.CTkFont(size=12),
                         text_color=COLORS["muted"]).pack(anchor="w", padx=14)
            ctk.CTkLabel(card, text="💡 "+r["explanation"], font=ctk.CTkFont(size=11),
                         text_color=COLORS["warning"], wraplength=900, justify="right").pack(anchor="w", padx=14, pady=(4,10))

        btn_row = ctk.CTkFrame(scroll, fg_color="transparent")
        btn_row.pack(fill="x", pady=20)
        ctk.CTkButton(btn_row, text="🔁 آزمون مجدد", command=lambda e=self.current_exam: self.start_exam(e),
                      fg_color=COLORS["accent2"], hover_color=COLORS["accent"],
                      text_color="white", width=140, height=40, corner_radius=10,
                      font=ctk.CTkFont(weight="bold")).pack(side="right", padx=6)
        ctk.CTkButton(btn_row, text="🏠 داشبورد", command=self.show_dashboard,
                      fg_color=COLORS["card_hover"], hover_color=COLORS["border"],
                      text_color=COLORS["text"], width=140, height=40, corner_radius=10).pack(side="right", padx=6)

    # ----------------------------------------------------------------
    # BOOKS (Reference list)
    # ----------------------------------------------------------------
    def show_books(self):
        self.clear_content()
        scroll = self.make_scroll(self.content)
        self.header(scroll, "📖 کتاب‌های مرجع مهندسی پزشکی (ارشد)",
                    "کتاب‌های اصلی و معتبری که برای کنکور ارشد باید مطالعه کنید — به همراه توضیح و کاربرد")

        BOOKS = [
            {"title":"Medical Instrumentation: Application and Design", "author":"John G. Webster",
             "topic":"ابزار دقیق پزشکی", "desc":"کتاب مرجع اصلی درس تجهیزات پزشکی؛ الکترودها، تقویت بیوپتانسیل، ECG/EEG/EMG، ایمنی الکتریکی، فشار، گلوکومتر، دیفیبریلاتور و…"},
            {"title":"Biomaterials Science: An Introduction to Materials in Medicine", "author":"Ratner, Hoffman, Schoen, Lemons",
             "topic":"بیومواد", "desc":"مرجع کلاسیک بیومواد؛ دسته‌بندی، زیست‌سازگاری، فلزات، سرامیک، پلیمرها، هیدروژل، کاربردهای ایمپلنت و مهندسی بافت."},
            {"title":"Biomechanics: Mechanical Properties of Living Tissues", "author":"Y.C. Fung",
             "topic":"بیومکانیک", "desc":"از کتاب‌های بنیادین بیومکانیک؛ خواص مکانیکی بافت، جریان خون، ویسکوالاستیسیته، ویژگی‌های استخوان، عضله، عروق."},
            {"title":"Basic Orthopaedic Biomechanics", "author":"Mow & Hayes",
             "topic":"بیومکانیک ارتوپدی", "desc":"مفصل ران/زانو، غضروف، تاندون، لیگامان، بیومکانیک ایمپلنت، سایش و خستگی."},
            {"title":"The Biomedical Engineering Handbook", "author":"Joseph Bronzino (Ed.)",
             "topic":"مرجع کلی مهندسی پزشکی", "desc":"هندبوک جامع روی بیشتر موضوعات BME؛ سیگنال، تصویربرداری، بیومکانیک، بیومواد، ابزار دقیق، سیستم‌های فیزیولوژیکی."},
            {"title":"Signals and Systems", "author":"Alan V. Oppenheim, Alan Willsky",
             "topic":"سیگنال‌ها و سیستم‌ها", "desc":"مرجع استاندارد سیگنال؛ فوریه، لاپلاس، Z، نمونه‌برداری، فیلترها. کتاب اطرش شاهافی/مارل برای کنکور ایران نیز رایج است."},
            {"title":"Signals and Systems for Bioengineers", "author":"John Semmlow",
             "topic":"سیگنال‌های زیستی", "desc":"نگرش کاربردی به سیگنال برای مهندسان پزشک؛ ECG, EEG, filter design, MATLAB examples."},
            {"title":"Digital Signal Processing", "author":"John G. Proakis, Dimitris Manolakis",
             "topic":"پردازش دیجیتال سیگنال", "desc":"مرجع DSP؛ FIR/IIR filters, FFT, window design; برای پردازش سیگنال پزشکی ضروری."},
            {"title":"Physiology (Guyton & Hall)", "author":"Guyton & Hall",
             "topic":"فیزیولوژی پزشکی", "desc":"کتاب فیزیولوژی کلاسیک؛ قلب، گردش خون، تنفس، عصب، کلیه، غدد — مرجع اصلی درس فیزیولوژی برای کنکور BME."},
            {"title":"Gray's Anatomy for Students", "author":"Drake, Vogl, Mitchell",
             "topic":"آناتومی", "desc":"آناتومی مدرن و تصویری برای درک ساختار بدن، قلب، اعصاب، اسکلت و مفاصل."},
            {"title":"Feedback Control of Dynamic Systems", "author":"Franklin, Powell, Emami-Naeini",
             "topic":"کنترل سیستم‌ها", "desc":"مرجع استاندارد کنترل؛ مدل‌سازی، پایداری، پاسخ فرکانسی، PID، طراحی کنترل‌کننده — پایه درس کنترل."},
            {"title":"Introduction to Biomedical Engineering", "author":"Enderle, Bronzino",
             "topic":"مقدمه مهندسی پزشکی", "desc":"درس‌نامه مقدماتی جامع که تقریباً همه سرفصل‌ها را پوشش می‌دهد؛ برای شروع عالی است."},
            {"title":"The Physics of Radiation Therapy", "author":"Faiz M. Khan",
             "topic":"پرتوشناسی و رادیوتراپی", "desc":"فیزیک پرتو در درمان سرطان، دوزیمتری، MV/KV X-ray, براکی‌تراپی."},
            {"title":"Bushberg's The Essential Physics of Medical Imaging", "author":"Bushberg et al.",
             "topic":"تصویربرداری پزشکی", "desc":"مرجع استاندارد فیزیک تصویربرداری؛ X-ray, CT, اولتراسوند، MRI، پزشکی هسته‌ای، دوز و ایمنی."},
            {"title":"Electric Circuits", "author":"James Nilsson, Susan Riedel",
             "topic":"مدارهای الکتریکی", "desc":"مدار ۱ و ۲؛ تونن/نورتن، آپ‌اَمپ، فازور، سه‌فاز، فیلتر، پاسخ فرکانسی."},
            {"title":"Fundamentals of Electric Circuits", "author":"Charles Alexander, Matthew Sadiku",
             "topic":"مدار", "desc":"کتاب مدار روان و پر از مثال؛ برای مباحث آپ‌اَمپ و مدار AC/DC مناسب."},
            {"title":"Differential Equations and Linear Algebra", "author":"C. Henry Edwards, David Penney",
             "topic":"ریاضیات (معادلات دیفرانسیل)", "desc":"مرجع معادلات دیفرانسیل معمولی و جبر خطی؛ برای درس ریاضی ۱ و معادلات دیفرانسیل."},
            {"title":"Advanced Engineering Mathematics", "author":"Erwin Kreyszig",
             "topic":"ریاضیات مهندسی", "desc":"مشتقات جزئی، فوریه، لاپلاس، اعداد مختلط، آمار؛ از مراجع رایج ریاضی مهندسی."},
            {"title":"Probability and Statistics for Engineering", "author":"Jay Devore",
             "topic":"آمار و احتمال", "desc":"آمار مهندسی، توزیع‌ها، آزمون فرض، رگرسیون، مباحث پایه آمار کنکور."},
            {"title":"مهندسی پزشکی (کتاب فارسی)", "author":"دکتر پرویز کاظمی / دکتر محمدرضا یکانی",
             "topic":"منابع فارسی", "desc":"کتاب‌های فارسی متعددی برای دروس مهندسی پزشکی وجود دارند (انتشارات دانشگاهی، مدرسان شریف، پارسه) که برای مرور نکات کنکوری مناسب‌اند."},
        ]

        for b in BOOKS:
            card = ctk.CTkFrame(scroll, fg_color=COLORS["card"], corner_radius=12)
            card.pack(fill="x", pady=6)
            head = ctk.CTkFrame(card, fg_color="transparent")
            head.pack(fill="x", padx=16, pady=(12,4))
            ctk.CTkLabel(head, text="📘", font=ctk.CTkFont(size=26)).pack(side="left", padx=(0,10))
            ctk.CTkLabel(head, text=b["title"], font=ctk.CTkFont(size=15, weight="bold"),
                         text_color=COLORS["accent"]).pack(side="left")
            ctk.CTkLabel(head, text=b["topic"], font=ctk.CTkFont(size=11),
                         fg_color=COLORS["accent2"], text_color="white",
                         corner_radius=8, width=160).pack(side="right", ipadx=6, ipady=3)
            ctk.CTkLabel(card, text=f"نویسنده(ها): {b['author']}", font=ctk.CTkFont(size=12),
                         text_color=COLORS["muted"]).pack(anchor="w", padx=16)
            ctk.CTkLabel(card, text=b["desc"], font=ctk.CTkFont(size=12),
                         text_color=COLORS["text"], wraplength=900, justify="right").pack(anchor="w", padx=16, pady=(4,12))

    # ----------------------------------------------------------------
    # BOOKMARKS
    # ----------------------------------------------------------------
    def show_bookmarks(self):
        self.clear_content()
        scroll = self.make_scroll(self.content)
        self.header(scroll, "⭐ نشان‌شده‌ها", "فصول یا سوالاتی که نشان کرده‌اید")
        bms = self.progress.get("bookmarks", [])
        if not bms:
            ctk.CTkLabel(scroll, text="هنوز چیزی نشان نشده. از داخل درس‌نامه روی ☆ نشان کردن بزن.",
                         font=ctk.CTkFont(size=14), text_color=COLORS["muted"]).pack(pady=40)
            return
        for b in bms:
            card = ctk.CTkFrame(scroll, fg_color=COLORS["card"], corner_radius=12)
            card.pack(fill="x", pady=6)
            ctk.CTkLabel(card, text="⭐ " + b.get("title","(بی‌نام)"), font=ctk.CTkFont(size=14, weight="bold"),
                         text_color=COLORS["warning"]).pack(anchor="w", padx=16, pady=(10,4))
            txt = ctk.CTkTextbox(card, fg_color="#0f172a", text_color=COLORS["text"],
                                 font=ctk.CTkFont(size=12), height=120, wrap="word", corner_radius=8)
            txt.pack(fill="x", padx=16, pady=(0,10))
            txt.insert("1.0", b.get("content",""))
            txt.configure(state="disabled")

    # ----------------------------------------------------------------
    # SETTINGS
    # ----------------------------------------------------------------
    def show_settings(self):
        self.clear_content()
        scroll = self.make_scroll(self.content)
        self.header(scroll, "⚙️ تنظیمات", "ظاهر و اطلاعات برنامه")

        ctk.CTkLabel(scroll, text="حالت نمایش", font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=COLORS["text"]).pack(anchor="w", pady=(10,6))
        seg = ctk.CTkSegmentedButton(scroll, values=["Dark", "Light", "System"],
                                     command=self._change_theme,
                                     fg_color=COLORS["card"], selected_color=COLORS["accent"],
                                     selected_hover_color=COLORS["accent2"])
        seg.pack(anchor="w")
        seg.set("Dark")

        ctk.CTkLabel(scroll, text="درباره برنامه", font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=COLORS["text"]).pack(anchor="w", pady=(24,6))
        ctk.CTkLabel(scroll,
            text="اپلیکیشن آمادگی کنکور کارشناسی ارشد مهندسی پزشکی\n"
                 "نسخه ۱.۰ — شامل ۱۲ درس اصلی، ده‌ها فصل درس‌نامه، بانک سوال، "
                 "و ۱۰ دوره آزمون جامع شبیه‌سازی‌شده.\n\n"
                 "پیشنهادات و گزارش اشکال را از طریق بخش نظرات بفرمایید.\n"
                 "موفق باشی! 🩺📚",
            font=ctk.CTkFont(size=13), text_color=COLORS["muted"], justify="left", wraplength=800).pack(anchor="w")

        ctk.CTkButton(scroll, text="🔄 ریست کامل پیشرفت", command=self.reset_progress,
                      fg_color=COLORS["danger"], hover_color="#dc2626",
                      text_color="white", width=200, height=38, corner_radius=8,
                      font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=20)

    def _change_theme(self, val):
        ctk.set_appearance_mode(val)

    def reset_progress(self):
        if messagebox.askyesno("تأیید", "آیا مطمئن هستید تمام پیشرفت شما پاک شود؟"):
            self.progress = {"bookmarks": [], "completed_lessons": [], "quiz_stats": {"correct":0,"total":0},
                             "exam_results": [], "last_opened": None}
            save_progress(self.progress)
            messagebox.showinfo("انجام شد", "پیشرفت پاک شد.")
            self.show_dashboard()


def run():
    app = BMEEngineeringApp()
    app.mainloop()


if __name__ == "__main__":
    run()
