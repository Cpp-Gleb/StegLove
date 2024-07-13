#include "dialogtoolrec.h"
#include "ui_dialogtoolrec.h"
#include <QFile>
#include <QTextStream>
#include <QIODevice>

DialogToolRec::DialogToolRec(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogToolRec)
{
    ui->setupUi(this);
    QFileInfo fi("./qw/binwalk.txt");
    QString fileName = fi.absoluteFilePath();
    QFile file(fileName);
    file.open(QFile::ReadOnly);
    QTextStream in(&file);
    ui->binwalk->setText(in.readAll());

    QFileInfo fi2("./qw/zsteg.txt");
    QString fileName2 = fi2.absoluteFilePath();
    QFile file2(fileName2);
    file2.open(QFile::ReadOnly);
    QTextStream in2(&file2);
    ui->zsteg->setText(in2.readAll());

    QFileInfo fi3("./qw/exiv2.txt");
    QString fileName3 = fi3.absoluteFilePath();
    QFile file3(fileName3);
    file3.open(QFile::ReadOnly);
    QTextStream in3(&file3);
    ui->exiv2->setText(in3.readAll());

    QFileInfo fi4("./qw/steghide.txt");
    QString fileName4 = fi4.absoluteFilePath();
    QFile file4(fileName4);
    file4.open(QFile::ReadOnly);
    QTextStream in4(&file4);
    ui->steghide->setText(in4.readAll());

    QFileInfo fi5("./qw/stegsolve.txt");
    QString fileName5 = fi5.absoluteFilePath();
    QFile file5(fileName5);
    file5.open(QFile::ReadOnly);
    QTextStream in5(&file5);
    ui->stegsolve->setText(in5.readAll());

    QFileInfo fi6("./qw/audacity.txt");
    QString fileName6 = fi6.absoluteFilePath();
    QFile file6(fileName6);
    file6.open(QFile::ReadOnly);
    QTextStream in6(&file6);
    ui->audacity->setText(in6.readAll());

    QFileInfo fi7("./qw/hexeditor.txt");
    QString fileName7 = fi7.absoluteFilePath();
    QFile file7(fileName7);
    file7.open(QFile::ReadOnly);
    QTextStream in7(&file7);
    ui->hexedit->setText(in7.readAll());

    QFileInfo fi8("./qw/stegolsb.txt");
    QString fileName8 = fi8.absoluteFilePath();
    QFile file8(fileName8);
    file8.open(QFile::ReadOnly);
    QTextStream in8(&file8);
    ui->stegolsb->setText(in8.readAll());
}

DialogToolRec::~DialogToolRec()
{
    delete ui;
}
