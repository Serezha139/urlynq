export PYTHONPATH="$PYTHONPATH:$(pwd)"
python pipelines/save_users.py
python pipelines/generate_recommendations.py
