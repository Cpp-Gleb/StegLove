#ifndef CONSOLEWIDGET_H
#define CONSOLEWIDGET_H

#include <QWidget>
#include <QTextEdit>
#include <QVBoxLayout>

class ConsoleWidget : public QWidget
{
    Q_OBJECT

public:
    explicit ConsoleWidget(QWidget *parent = nullptr);
    void appendText(const QString &text);

private:
    QTextEdit *outputArea;
};

#endif // CONSOLEWIDGET_H
