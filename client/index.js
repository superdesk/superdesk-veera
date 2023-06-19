import {startApp} from 'superdesk-core/scripts/index';

setTimeout(() => {
    startApp(
        [
            {
                id: 'annotationsLibrary',
                load: () => import('superdesk-core/scripts/extensions/annotationsLibrary'),
            },
            {
                id: 'markForUser',
                load: () => import('superdesk-core/scripts/extensions/markForUser'),
            },
            {
                id: 'datetimeField',
                load: () => import('superdesk-core/scripts/extensions/datetimeField'),
            },
        ],
        {},
    );
});

export default angular.module('main.superdesk', []);
