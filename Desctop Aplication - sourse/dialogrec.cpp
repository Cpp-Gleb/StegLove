#include "dialogrec.h"
#include "ui_dialogrec.h"
#include <QFile>
#include <QTextStream>
#include <QIODevice>


DialogRec::DialogRec(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogRec)
{
    ui->setupUi(this);

    QString str= "./qw/CommonRec";
    QFileInfo fi(str + ".txt");
    QString fileName = fi.absoluteFilePath();
    QFile file(fileName);
    file.open(QFile::ReadOnly);
    QTextStream in(&file);
    ui->Label_com->setText((in.readAll()));
}



DialogRec::~DialogRec()
{
    delete ui;
}
