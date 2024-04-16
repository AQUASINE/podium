<script setup>
import {computed, onMounted, ref} from 'vue';
import * as THREE from 'three';
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader';
import {useStore} from "vuex";

const threeContainer = ref(null);
const threeContainerParent = ref(null);
const objectPath = "/mrpodium.glb";

const store = useStore();

const users = computed(() => store.state.users);
const worstChatter = computed(() => {
  if (users.value.length === 0) {
    return null;
  }
  return users.value[users.value.length - 1];
});

onMounted(() => {
  const rect = threeContainerParent.value.getBoundingClientRect();
  console.log(rect.width, rect.height);
  const scene = new THREE.Scene();
  const renderer = new THREE.WebGLRenderer();
  // get size of the container
  renderer.setSize(rect.width, rect.height);
  let camera;

  window.addEventListener('resize', () => {
    const rect = threeContainerParent.value.getBoundingClientRect();
    if (camera) {
      camera.aspect = rect.width / rect.height;
      camera.updateProjectionMatrix();
    }
    renderer.setSize(rect.width, rect.height);
  });


  threeContainer.value.appendChild(renderer.domElement);

  let mrPodium;
  const loader = new GLTFLoader();
  let animations = [];
  let mixer;
  let cameraRotationStartX;
  let cameraRotationStartY;
  loader.load(objectPath, function (gltf) {
    mrPodium = gltf.scene;
    camera = gltf.cameras[0];
    animations = gltf.animations;
    camera.aspect = rect.width / rect.height;
    camera.updateProjectionMatrix();
    cameraRotationStartY = camera.rotation.y;
    cameraRotationStartX = camera.rotation.x;
    scene.add(mrPodium);
    console.log(gltf);

    // find all point lights and set their intensity to 0.5
    mrPodium.traverse((child) => {
      if (child.isPointLight) {
        child.intensity *= 0.008;
      }
    });

    // play animations
    mixer = new THREE.AnimationMixer(mrPodium);
    animations.forEach((clip) => {
      mixer.clipAction(clip).play();
    });
  });

  const geometry = new THREE.BoxGeometry();
  const material = new THREE.MeshBasicMaterial({color: 0x00ff00});
  const cube = new THREE.Mesh(geometry, material);
  scene.add(cube);

  // set background to transparent
  renderer.setClearColor(0x000000, 0);


  let phase = 0;
  const animate = function () {
    requestAnimationFrame(animate);

    if (mrPodium) {
      mrPodium.scale.set(0.01, 0.01, 0.01);
      mrPodium.rotation.y = -90;
    }

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    if (mixer) {
      mixer.update(0.005);
    }

    if (camera) {
      phase += 0.01;
      camera.rotation.x = cameraRotationStartX + Math.sin(phase) * 0.001;
      renderer.render(scene, camera);
    }
  };

  animate();
});

</script>

<template>
  <div class="container__presentation-mode">
    <div class="container__message-box-wrapper">
      <div class="container__message-box">
        <div>
          Our worst chatter is:
        </div>
        <div v-if="worstChatter">

          <div class="container__big-name">
            {{ worstChatter.user }}
          </div>
          <div>
            with a score of {{ worstChatter.user_score }}
          </div>
        </div>
      </div>
    </div>
    <div class="container__presentation-mode-view" ref="threeContainerParent">
      <div ref="threeContainer" class="container__three"></div>
    </div>
  </div>
</template>

<style scoped>
.container__presentation-mode-view {
  width: 100%;
  height: 100%;
  min-height: calc(100vh - 10rem);
  max-height: calc(100vh - 10rem);
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  bottom: 0;
  left: -100px;
  z-index: 1;
}

.container__three {
}

.container__message-box {
  background-color: var(--bg3);
  padding: 1rem;
  border-radius: 0.25rem;
  margin: 1rem;
  text-align: center;
}

.container__big-name {
  font-size: 2em;
  font-weight: 700;
}

.container__message-box-wrapper {
  height: 0;
}
</style>