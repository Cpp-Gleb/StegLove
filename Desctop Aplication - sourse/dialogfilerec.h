#ifndef DIALOGFILEREC_H
#define DIALOGFILEREC_H

#include <QDialog>
#include <QtWidgets>
namespace Ui {
class DialogFileRec;
}

class DialogFileRec : public QDialog
{
    Q_OBJECT

public:
    explicit DialogFileRec(QWidget *parent = nullptr);
    ~DialogFileRec();

private:
    Ui::DialogFileRec *ui;
};

#endif // DIALOGFILEREC_H
