#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtWidgets>
#include "scaledpixmap.h"



QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    QString _mask;
    QString _fileName;

private slots:
    void slotOpenFile();
    void slotAbout();
    void slotRecomendCom();
    void slotRecomendFile();
    void slotRecomendTool();
    void slotReadForFile();
    void slotSwitchFormat();
    void on_ButtonFormat_clicked();
    void on_ButtonMore_clicked();

};


#endif // MAINWINDOW_H
