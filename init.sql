-- create requirements
USE your_database_name;
INSERT INTO requirements_requirements VALUE(1, 'TODOアプリを作ろう', '要件テキスト', 0, 'A', '1', '2025-11-1', '2025-11-1', '{users_id}', 'low');
INSERT INTO requirements_requirements VALUE(2, 'チャットアプリを作ろう', '要件テキスト', 0, 'A', '1', '2025-11-1', '2025-11-1', '{users_id}', 'mid');
INSERT INTO requirements_requirements VALUE(3, '勤怠管理システム制作', '要件テキスト', 0, 'A', '1', '2025-11-1', '2025-11-1', '{users_id}', 'high');
INSERT INTO requirements_requirements VALUE(4, 'サイバーセキュリティ学習環境の制作', '要件テキスト', 0, 'A', '1', '2025-11-1', '2025-11-1', '{users_id}', 'high');

-- create articles
INSERT INTO requirements_articles VALUE(1, 'frontend', 'HTMLについて学ぼう', 'https://raretech.site/dashboard/step/91', '2025-11-1', '2025-11-1', 1);
INSERT INTO requirements_articles VALUE(2, 'frontend', 'CSSについて学ぼう', 'https://raretech.site/dashboard/step/93', '2025-11-1', '2025-11-1', 1);
INSERT INTO requirements_articles VALUE(3, 'frontend', 'JavaScriptについて学ぼう', 'https://envader.plus/article/331', '2025-11-1', '2025-11-1', 1);
INSERT INTO requirements_articles VALUE(4, 'backend', 'プログラミングハンズオンに挑戦しよう Part1', 'https://raretech.site/dashboard/step/126', '2025-11-1', '2025-11-1', 1);
INSERT INTO requirements_articles VALUE(5, 'backend', 'GETとPOSTの違いについて学習しよう', 'https://raretech.site/dashboard/step/146', '2025-11-1', '2025-11-1', 1);
INSERT INTO requirements_articles VALUE(6, 'infra', 'GitHubをはじめよう', 'https://raretech.site/dashboard/step/76', '2025-11-1', '2025-11-1', 1);
INSERT INTO requirements_articles VALUE(7, 'infra', 'GitとGitHubを使ってみよう', 'https://raretech.site/dashboard/step/77', '2025-11-1', '2025-11-1', 1);

-- create tech_stacks
INSERT INTO requirements_tech_stacks VALUE(1, 'HTML', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/html-5_5968267.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(2, 'CSS', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/css-3_5968242.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(3, 'JavaScript', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/js_5968292.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(4, 'Python', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/python-logo-only.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(5, 'Flask', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/icons8-%E3%83%95%E3%83%A9%E3%82%B9%E3%82%B3-100.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(6, 'Django', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/django-logo-negative.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(7, 'Java', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/icons8-java-coffee-cup%E3%81%AE%E3%83%AD%E3%82%B3%E3%82%99-96.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(8, 'Quarkus', 'https://hackathon-dev-image-dteam.s3.ap-northeast1.amazonaws.com/quarkus_icon_512px_default.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(9, 'MySQL', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/logo-mysql-170x115.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(10, 'Postgre', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/elephant.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(11, 'Docker', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/docker-mark-blue.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(12, 'AWS', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/icons8-aws-96.png', '2025-11-01', '2025-11-01');
INSERT INTO requirements_tech_stacks VALUE(13, 'Teraform', 'https://hackathon-dev-image-dteam.s3.ap-northeast-1.amazonaws.com/icons8-%E3%83%86%E3%83%A9%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0-96.png', '2025-11-01', '2025-11-01');

-- create requirements_tech_stacks
INSERT INTO requirements_requirements_tech_stacks VALUE(1, '2025-11-01', '2025-11-01', 1, 1);
INSERT INTO requirements_requirements_tech_stacks VALUE(2, '2025-11-01', '2025-11-01', 1, 2);
INSERT INTO requirements_requirements_tech_stacks VALUE(3, '2025-11-01', '2025-11-01', 1, 4);
INSERT INTO requirements_requirements_tech_stacks VALUE(4, '2025-11-01', '2025-11-01', 1, 5);
INSERT INTO requirements_requirements_tech_stacks VALUE(5, '2025-11-01', '2025-11-01', 1, 9);
INSERT INTO requirements_requirements_tech_stacks VALUE(6, '2025-11-01', '2025-11-01', 1, 11);
INSERT INTO requirements_requirements_tech_stacks VALUE(7, '2025-11-01', '2025-11-01', 2, 1);
INSERT INTO requirements_requirements_tech_stacks VALUE(8, '2025-11-01', '2025-11-01', 2, 2);
INSERT INTO requirements_requirements_tech_stacks VALUE(9, '2025-11-01', '2025-11-01', 2, 3);
INSERT INTO requirements_requirements_tech_stacks VALUE(10, '2025-11-01', '2025-11-01', 2, 4);
INSERT INTO requirements_requirements_tech_stacks VALUE(11, '2025-11-01', '2025-11-01', 2, 5);
INSERT INTO requirements_requirements_tech_stacks VALUE(12, '2025-11-01', '2025-11-01', 2, 9);
INSERT INTO requirements_requirements_tech_stacks VALUE(13, '2025-11-01', '2025-11-01', 2, 11);
INSERT INTO requirements_requirements_tech_stacks VALUE(14, '2025-11-01', '2025-11-01', 3, 1);
INSERT INTO requirements_requirements_tech_stacks VALUE(15, '2025-11-01', '2025-11-01', 3, 2);
INSERT INTO requirements_requirements_tech_stacks VALUE(16, '2025-11-01', '2025-11-01', 3, 3);
INSERT INTO requirements_requirements_tech_stacks VALUE(17, '2025-11-01', '2025-11-01', 3, 4);
INSERT INTO requirements_requirements_tech_stacks VALUE(18, '2025-11-01', '2025-11-01', 3, 6);
INSERT INTO requirements_requirements_tech_stacks VALUE(19, '2025-11-01', '2025-11-01', 3, 9);
INSERT INTO requirements_requirements_tech_stacks VALUE(20, '2025-11-01', '2025-11-01', 3, 11);
INSERT INTO requirements_requirements_tech_stacks VALUE(21, '2025-11-01', '2025-11-01', 3, 12);
INSERT INTO requirements_requirements_tech_stacks VALUE(22, '2025-11-01', '2025-11-01', 4, 1);
INSERT INTO requirements_requirements_tech_stacks VALUE(23, '2025-11-01', '2025-11-01', 4, 2);
INSERT INTO requirements_requirements_tech_stacks VALUE(24, '2025-11-01', '2025-11-01', 4, 3);
INSERT INTO requirements_requirements_tech_stacks VALUE(25, '2025-11-01', '2025-11-01', 4, 7);
INSERT INTO requirements_requirements_tech_stacks VALUE(26, '2025-11-01', '2025-11-01', 4, 8);
INSERT INTO requirements_requirements_tech_stacks VALUE(27, '2025-11-01', '2025-11-01', 4, 10);
INSERT INTO requirements_requirements_tech_stacks VALUE(28, '2025-11-01', '2025-11-01', 4, 11);
INSERT INTO requirements_requirements_tech_stacks VALUE(29, '2025-11-01', '2025-11-01', 4, 12);
INSERT INTO requirements_requirements_tech_stacks VALUE(30, '2025-11-01', '2025-11-01', 4, 13);

-- create questions
INSERT INTO questions VALUE(1, 'ハッカソンの進め方について', 'A', 'インフラ', 'ハッカソンの進め方がわからないです。・何から進めていけばいいのか・どういった手順で進めていけばいいのか・いつまでに何を終えていればいいのかを教えていただきたいです。また、注意事項などがあればそちらも教えていただきたいです。', false, '2025-11-01', '2025-11-01', '{users_id}');
INSERT INTO questions VALUE(2, 'git add, git commit, git pushの違いについて', 'B', 'インフラ', '内容テキストテキスト', true, '2025-11-01', '2025-11-01', '{users_id}');
INSERT INTO questions VALUE(3, 'ハッカソンのリーダーの仕事とは？', 'C', 'インフラ', '内容テキストテキスト', false, '2025-11-01', '2025-11-01', '{users_id}');
INSERT INTO questions VALUE(4, 'ローカルリポジトリとリモートリポジトリについて', 'A', 'インフラ', '内容テキストテキスト', true, '2025-11-01', '2025-11-01', '{users_id}');
INSERT INTO questions VALUE(5, 'ER図は何を元に考えていけばいいか', 'B', 'バックエンド', '内容テキストテキスト', false, '2025-11-01', '2025-11-01', '{users_id}');
INSERT INTO questions VALUE(6, 'gitで間違えてcommitしてしまった時の対処法', 'C', 'フロントエンド', '内容テキストテキスト', true, '2025-11-01', '2025-11-01', '{users_id}');

-- create answers
INSERT INTO answers_answers VALUE(1, 'お疲れ様です！昨年度から毎月ハッカソンに参加しているものです。ハッカソン始まったはいいですが、何から進めていけばいいのか不安ですよね...！ハッカソンの種類によりますが、手順は以下の通りです！・要件が決まっているもの１.リーダーを決める２.ポジションを決める・要件が決まっていないもの１.リーダーを決める２.ポジションを決めるこのような形で進めていけばいいと思います！！初は何が何だかわからないと思いますが、頑張ってください！', '2025-11-01', '2025-11-01', 1, '{users_id}');
INSERT INTO answers_answers VALUE(2, 'こちらのURLに詳しく書いているので、参考にしてみてください。https://example.com', '2025-11-01', '2025-11-01', 1, '{users_id}');
INSERT INTO answers_answers VALUE(3, '説明テキストテキスト', '2025-11-01', '2025-11-01', 2, '{users_id}');