INSERT INTO accounts_user (
    id, password, last_login, is_superuser, date_joined, email, first_name, last_name, is_active, type_choice
) VALUES
(1, 'pbkdf2_sha256$320000$YETpIYW49w1sVigoPVlVEj$mH', '2022-03-08 19:00:56.271280', 1, '2022-03-08 19:00:56.271280', 'admin@email.com', 'Emge', 'One', 1, 1),
(2, 'pbkdf2_sha256$320000$YETpIYW49w1sVigoPVlVEj$mH+OHXjLmKkl5QkqASsnJ7RzKdk+ChRkYftsit6oYlA=', NULL, 0, '2022-03-08 19:00:56.271280', 'staff@email.com', 'Mike', 'Staff', 1, 2),
(3, 'pbkdf2_sha256$320000$YETpIYW49w1sVigoPVlVEj$mH+OHXjLmKkl5QkqASsnJ7RzKdk+ChRkYftsit6oYlA=', NULL, 0, '2022-03-08 19:00:56.271280', 'merchant@email.com', 'Ann', 'Merchant', 1, 3),
(4, 'pbkdf2_sha256$320000$YETpIYW49w1sVigoPVlVEj$mH+OHXjLmKkl5QkqASsnJ7RzKdk+ChRkYftsit6oYlA=', NULL, 0, '2022-03-08 19:00:56.271280', 'customer@email.com', 'Jean', 'Customer', 1, 4);
