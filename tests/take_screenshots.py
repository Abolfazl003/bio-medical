"""گرفتن اسکرین‌شات‌های v1.3 برای بازبینی ظاهر"""
from playwright.sync_api import sync_playwright
OUT = "/home/user/shots4/"
with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={"width":1440,"height":950})
    pg.goto("http://127.0.0.1:8000/index.html"); pg.wait_for_timeout(900)
    # داده نمونه تا نمودارها خالی نباشند
    pg.evaluate("""(()=>{
      const L=STATE.progress.daily_log||(STATE.progress.daily_log={});
      const vals=[22,35,44,0,58,40,52,30,64,48,0,36,50,42];
      vals.forEach((v,i)=>{ const d=new Date(Date.now()-(13-i)*86400000);
        L[d.toISOString().slice(0,10)]=v; });
      STATE.progress.completed_lessons = ['circuits:circ-c1','circuits:circ-c2','math:math-c1','math:math-c3','imaging:img-c1','anatomy:ana-c1','control:ctrl-c1'];
      STATE.progress.quiz_stats={correct:41,total:52};
      saveProgress();
    })()""")
    pg.wait_for_timeout(200)
    pg.evaluate("setView('progress')"); pg.wait_for_timeout(700)
    pg.screenshot(path=OUT+"d-progress.png")
    pg.evaluate("setView('teacher')"); pg.wait_for_timeout(600)
    pg.screenshot(path=OUT+"d-teacher-home.png")
    pg.evaluate("openTeacher('circuits')"); pg.wait_for_timeout(700)
    pg.screenshot(path=OUT+"d-lecture.png")
    pg.evaluate("for(let i=0;i<12;i++) STATE.teacher.slide++; render();"); pg.wait_for_timeout(500)
    pg.screenshot(path=OUT+"d-lecture2.png")
    pg.evaluate("openTeacherBook('img-mri')"); pg.wait_for_timeout(600)
    pg.evaluate("STATE.teacher.slide=3; render();"); pg.wait_for_timeout(400)
    pg.screenshot(path=OUT+"d-lecture-book.png")
    pg.evaluate("showJozve('cir-transient')"); pg.wait_for_timeout(700)
    pg.screenshot(path=OUT+"d-jozve.png")
    pg.evaluate("window.scrollTo?0:0; document.querySelector('#main').scrollTop=1200;"); pg.wait_for_timeout(400)
    pg.screenshot(path=OUT+"d-jozve2.png")
    pg.evaluate("showJozveSubject('signals')"); pg.wait_for_timeout(700)
    pg.screenshot(path=OUT+"d-jozve-sub.png")
    pg.evaluate("openBookHome('circuits')"); pg.wait_for_timeout(600)
    pg.screenshot(path=OUT+"d-shelf.png")
    pg.evaluate("setView('books')"); pg.wait_for_timeout(600)
    pg.screenshot(path=OUT+"d-books.png")
    pg.evaluate("openBookHome('circuits',1? 'cir-basic':'cir-basic')"); pg.wait_for_timeout(500)
    pg.evaluate("openBookChapter('math','math-c5')"); pg.wait_for_timeout(700)
    pg.screenshot(path=OUT+"d-book-fig.png")
    pg.evaluate("openBookChapter('circuits','circ-c1')"); pg.wait_for_timeout(600)
    pg.screenshot(path=OUT+"d-book-fig2.png")
    pg.evaluate("setView('dashboard')"); pg.wait_for_timeout(600)
    pg.screenshot(path=OUT+"d-dashboard.png")
    b.close()
print("done")
