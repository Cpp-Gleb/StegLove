#include "dialogfilerec.h"
#include "ui_dialogfilerec.h"
#include <QFile>
#include <QTextStream>
#include <QIODevice>


DialogFileRec::DialogFileRec(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogFileRec)
{
    ui->setupUi(this);

    QFileInfo fi("./qw/png.txt");
    QString fileName = fi.absoluteFilePath();
    QFile file(fileName);
    file.open(QFile::ReadOnly);
    QTextStream in(&file);
    ui->png->setText(in.readAll());

    QFileInfo fi2("./qw/jpg.txt");
    QString fileName2 = fi2.absoluteFilePath();
    QFile file2(fileName2);
    file2.open(QFile::ReadOnly);
    QTextStream in2(&file2);
    ui->jpg->setText(in2.readAll());

    QFileInfo fi3("./qw/wav.txt");
    QString fileName3 = fi3.absoluteFilePath();
    QFile file3(fileName3);
    file3.open(QFile::ReadOnly);
    QTextStream in3(&file3);
    ui->wav->setText(in3.readAll());

    QFileInfo fi4("./qw/doc.txt");
    QString fileName4 = fi4.absoluteFilePath();
    QFile file4(fileName4);
    file4.open(QFile::ReadOnly);
    QTextStream in4(&file4);
    ui->doc->setText(in4.readAll());
}

DialogFileRec::~DialogFileRec(){
    delete ui;
}
