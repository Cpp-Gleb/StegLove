#ifndef DIALOGTOOLREC_H
#define DIALOGTOOLREC_H

#include <QDialog>
#include <QtWidgets>
namespace Ui {
class DialogToolRec;
}

class DialogToolRec : public QDialog
{
    Q_OBJECT

public:
    explicit DialogToolRec(QWidget *parent = nullptr);
    ~DialogToolRec();

private:
    Ui::DialogToolRec *ui;
};

#endif // DIALOGTOOLREC_H
