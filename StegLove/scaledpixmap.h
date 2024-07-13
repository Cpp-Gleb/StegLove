#ifndef SCALEDPIXMAP_H
#define SCALEDPIXMAP_H
#include <QtWidgets>

class ScaledPixmap : public QWidget {
public:
  ScaledPixmap(QWidget *parent = 0);
  void setScaledPixmap(const QPixmap &pixmap);
  QSize sizeHint() const;
  void setText(QString());
protected:
  void paintEvent(QPaintEvent *event);
private:
  QPixmap m_pixmap;
};

#endif // SCALEDPIXMAP_H
