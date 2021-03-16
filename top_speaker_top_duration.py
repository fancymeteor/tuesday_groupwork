%run helpers.py
videos_df = pd.read_csv(VIDEO_CSV)
clustering_helper = ClusteringHelper('hdbscan')
#clustering_helper.save_timeline("timeline_groupwork/", verbose=True)
# Plot clusters
#clustering_helper.plot_clusters(video_id='BkAyeWznYB0', n=64)
#for i in range(len(videos.id)):
duration_by_speaker = clustering_helper.get_top_speakers("timelines")
top_duration = duration_by_speaker.sort_values(ascending=False).head(10)
top_speakers = list(top_duration.index)
print("Top duration by speaker:",top_duration)
print("Top speakers:",top_speakers)
