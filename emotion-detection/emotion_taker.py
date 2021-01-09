import visualize
emotion_array = visualize.visualizer()
emotion_array = np.array(emotion_array)
emotion_array = (emotion_array/sum(emotion_array))*100

plt.rcParams['figure.figsize'] = (13.5,5.5)
for i in range(len(emotion_array)):
    axes = plt.subplot(2, 4, i)
    emojis_img = io.imread('images/emojis/%s.png' % str(class_names[i]))
    plt.imshow(emojis_img)
    plt.xlabel(str(emotion_array(i)), fontsize=16)
    axes.set_xticks([])
    axes.set_yticks([])
plt.tight_layout()
plt.savefig(os.path.join('images/results/{}.png'.format(i+1)))
plt.close()
