#q3
SELECT owner.owner_id, owner.owner_name,  COUNT(category.category_title)
ORDER BY  COUNT(category.category_title)
WHERE owner.owner_id=article.owner_id AND article.article_id=category_article_mapping.article_id AND category_article_mapping.category_id=category.category_id
FROM owner,category, article,category_article_mapping

