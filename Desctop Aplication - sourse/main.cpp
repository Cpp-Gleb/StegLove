#include "mainwindow.h"

#include <QApplication>

void loadModules(QSplashScreen* psplash)
{
    QElapsedTimer time_;
    time_.start();

    for (int i = 0; i < 100; ) {
        if (time_.elapsed() > 40) {
            time_.start();
            ++i;
        }
        psplash->showMessage("Loading modules: "
                             + QString::number(i) + "%",
                             Qt::AlignHCenter | Qt::AlignBottom ,
                             Qt::white
                            );
    }
}

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QSplashScreen splash(QPixmap("preview.jpg").scaled(535,250));
    splash.show();
    loadModules(&splash);
    MainWindow w;
    splash.finish(&w);
    w.show();
    return a.exec();
}
