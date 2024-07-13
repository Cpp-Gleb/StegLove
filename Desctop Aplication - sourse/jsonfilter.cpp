#include <jsonfilter.h>

JsonPostRequester::JsonPostRequester(QObject *parent): QObject(parent)
    {
        connect(&manager, &QNetworkAccessManager::finished, this, &JsonPostRequester::onFinished);
    }

    void JsonPostRequester::sendPostRequest(const QUrl &url, const QJsonObject &json)
    {
        QNetworkRequest request(url);
        request.setHeader(QNetworkRequest::ContentTypeHeader, "application/json");

        QJsonDocument doc(json);
        QByteArray data = doc.toJson();

        QNetworkReply *reply = manager.post(request, data);
        connect(reply, &QNetworkReply::errorOccurred, this, &JsonPostRequester::onError);
    }


    void JsonPostRequester::onFinished(QNetworkReply *reply)
    {
        if (reply->error() == QNetworkReply::NoError) {
            QByteArray response_data = reply->readAll();
            QJsonDocument response_doc = QJsonDocument::fromJson(response_data);
            if (response_doc.isObject()) {
                QJsonObject response_object = response_doc.object();
                // Обработка JSON ответа
                qDebug() << "Response JSON:" << response_object;
                // Сохраните JSON ответ в переменную здесь
                this->jsonResponse = response_object;
            }
        }
        reply->deleteLater();
    }

    void JsonPostRequester::onError(QNetworkReply::NetworkError code)
    {
        qWarning() << "Network error:" << code;
    }



