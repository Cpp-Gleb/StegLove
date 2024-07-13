#include "jsonparser.h"
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonArray>
#include <QVBoxLayout>
#include <QLabel>
#include <QMessageBox>

JsonParser::JsonParser(QWidget *parent)
    : QObject(parent), parentWidget(parent) {
    networkManager = new QNetworkAccessManager(this);
    connect(networkManager, &QNetworkAccessManager::finished, this, &JsonParser::onNetworkReply);
}

void JsonParser::fetchJson(const QUrl &url) {
    QNetworkRequest request(url);
    networkManager->get(request);
}

void JsonParser::onNetworkReply(QNetworkReply *reply) {
    if (reply->error() != QNetworkReply::NoError) {
        QMessageBox::critical(parentWidget, "Network Error", reply->errorString());
        reply->deleteLater();
    }

    QByteArray responseData = reply->readAll();
    QJsonDocument jsonDoc = QJsonDocument::fromJson(responseData);
    if (jsonDoc.isNull() || !jsonDoc.isObject()) {
        QMessageBox::critical(parentWidget, "JSON Error", "Failed to parse JSON.");
        reply->deleteLater();
    }

    QJsonObject jsonObject = jsonDoc.object();
    emit jsonParsed(jsonObject);

    reply->deleteLater();
}
