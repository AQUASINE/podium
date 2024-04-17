import { ref } from 'vue';

export function useMessageLengthValidator(initialValue) {
    const value = ref(initialValue);

    const validate = () => {
        value.value = Math.floor(value.value);

        if (value.value < 1) {
            value.value = 1;
        }

        if (value.value > 1000) {
            value.value = 1000;
        }
    };

    return {
        value,
        validate
    };
}