from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def train_model(df, test_size=0.2, random_state=42):
    X = df[['age', 'time_on_site', 'pages_visited', 'is_returning']]
    y = df['buy']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    return model, X_test, y_test, y_pred

